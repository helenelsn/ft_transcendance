from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context, get_context
from relationship.models import FriendInvitation
from games.models import GameLaunching
from event.models import EventInvitation
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any
from .models import Notification, Invitation
from common.templatetags import html_utils
from django.utils.html import format_html
from common.views import ActionModelView
from common.views import BaseAppView, RedirDict, User, BasicModelView, ActionModelView
from django.urls import reverse

class NotificationsAppView(BaseAppView):
    app_name = 'notifications'

    def get_app_redirs(self, user : User) -> RedirDict:
        return RedirDict().add_page(self, page=('index','my realtions'), main_key=True).add_page(self, 'all', 'all users')

    def get_notif_view(self, object = None, user : User = None, pk : int = 0):
        notif_views = [FriendInvitationView, EventInvitationView, InvitationView, NotificationsView, ]
        
        for notif_view in notif_views:
            view : NotificationsView = notif_view(object=object, user=user, pk=pk)
            if view.object is not None:
                break

class NotificationsView(ActionModelView):
    app_view = NotificationsAppView()
    
    def __init__(self, object = None, user : User = None, pk : int = 0):
        if user is not None and pk > 0:
            object = get_object_or_404(user.notification_set.filter(pk=pk))
        super().__init__(object)
        self.user = user
        # self.object : Notification = object
     
    @property
    def user_notifs(self):
        return Notification.filter_user_notifs(self.user).all()
    
    @property
    def user_view(self) -> bool:
        return self.object is None and self.user is not None 
    
    def read(self, is_read : bool = True):
        if self.user_view:
            for notif in self.user_notifs:
                notif.is_read = is_read
                notif.save()
        else:
            self.object.is_read = is_read
            self.object.save()
        
        return self.index_view()

    def delete(self):
        if self.user_view:
            for notif in self.user_notifs:
                Notification.delete(notif.pk)
        else:
            Notification.delete(self.object.pk)
        return self.index_view()
    
    def get_user_actions_on_obj(self, user:User=None, all=False) -> RedirDict:
        d = RedirDict()
        d.add_dict(InvitationView(object=self.object).get_user_actions_on_obj(user))
        if all:
            d.add_dict(self.is_read_action())
            d.add_dict(self.delete_action())
        return d
    
    def add_action_to_dict(self, action : str, d = None) -> RedirDict:
        d = RedirDict() if d is None else d
        kwargs={'action' : action}
        display = action
        if not self.user_view:
            kwargs.update({'pk':self.object.pk})
        else:
            display = display + ' all'
            kwargs.update({'pk':0})
        return d.add(url=reverse(viewname=self.app_view.get_viewname('notif_act'), kwargs=kwargs), display=display)
            
    def add_actions_to_dict(self, actions : list, d = None) -> RedirDict:
        d = RedirDict() if d is None else d
        for action in actions:
            self.add_action_to_dict(action=action, d=d)
        return d
            
    def is_read_action(self, ) -> RedirDict:
        if self.user_view:
            return self.add_actions_to_dict(['read', 'unread'])
        if self.object.is_read :
            return self.add_action_to_dict('unread')
        else:
            return self.add_action_to_dict('read')
        
    def delete_action(self) -> RedirDict:
        return self.add_action_to_dict('delete')
    
    def get_actions_on_all(self) -> RedirDict:
        if not self.user_view:
            raise('Should be a user notification view to cal this')
        return RedirDict(self.is_read_action()).add_dict(self.delete_action())


class InvitationView(NotificationsView):
    model = Invitation
    def __init__(self, object=None, user = None, pk = 0):
        super().__init__(object, user, pk)
        if self.object is not None:
            if self.model.objects.filter(pk=self.object.pk).count() > 0:
                self.object = self.model.objects.get(pk=self.object.pk)
            else:
                self.object = None
        
    def get_user_actions_on_obj(self, user = None) -> RedirDict:
        if self.object is not None:
            return self.add_actions_to_dict(['accept', 'deny'])
        return RedirDict()
        
        

class FriendInvitationView(InvitationView):
    model = FriendInvitation
    
class EventInvitationView(InvitationView):
    model = EventInvitation
    
class GameLaunchingView(NotificationsView):
    @staticmethod
    def notif_react_action(notif : GameLaunching):
        return ""

        