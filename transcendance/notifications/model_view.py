from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context, get_context
from relationship.models import FriendInvitation
from games.models import GameLaunching
from event.models import EventInvitation
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any
from .models import Notification
from common.templatetags import html_utils
from django.utils.html import format_html
from common.views import ActionModelView
from common.views import BaseAppView, RedirDict, User, BasicModelView, ActionModelView
from django.urls import reverse

class NotificationsAppView(BaseAppView):
    app_name = 'notifications'

    def get_app_redirs(self, user : User) -> RedirDict:
        return RedirDict().add_page(self, page=('index','my realtions'), main_key=True).add_page(self, 'all', 'all users')


class NotificationsView(ActionModelView):
    app_view = NotificationsAppView()
    
    def __init__(self, object = None, user : User = None, pk : int = 0):
        if user is not None and pk > 0:
            object = get_object_or_404(user.notification_set.filter(pk=pk))
        super().__init__(object)
        self.user = user
        self.object : Notification = object
    
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
    
    def get_actions(self, user: User) -> RedirDict:
        return super().get_actions(user)
    
    def add_action(self, action : str, d = None) -> RedirDict:
        d = RedirDict() if d is None else d
        kwargs={'action' : action}
        display = action
        if not self.user_view:
            kwargs.update({'pk':self.object.pk})
        else:
            display = display + ' all'
            kwargs.update({'pk':0})
        return d.add(url=reverse(viewname=self.app_view.get_viewname('notif_act'), kwargs=kwargs), display=display)
            
    def add_actions(self, actions : list, d = None) -> RedirDict:
        d = RedirDict() if d is None else d
        for action in actions:
            self.add_action(action=action, d=d)
        return d
            
    def is_read_action(self, ) -> RedirDict:
        if self.user_view:
            return self.add_actions(['read', 'unread'])
        if self.object.is_read :
            return self.add_action('unread')
        else:
            return self.add_action('read')
        
    def delete_action(self) -> RedirDict:
        return self.add_action('delete')
    
    def get_actions_on_all(self) -> RedirDict:
        if not self.user_view:
            raise('Should be a user notification view to cal this')
        return RedirDict(self.is_read_action()).add_dict(self.delete_action())
        
    # @staticmethod
    # def notif_is_read_action(notif):
    #     actions = [
    #         ('read_notif' , 'mark read'),
    #         ('unread_notif' , 'mark unread')
    #     ]
    #     args=[notif.id]
    #     return NotificationsView(object=notif).is_read_action().get_html
    
    # @staticmethod
    # def notif_delete_action(notif):
    #     return html_utils.a_hyperlink(redir=f'notifications:delete_notif', display='delete', args=[notif.id])
    
    # @staticmethod
    # def notif_react_action(notif):
    #     if len(FriendInvitation.objects.filter(pk=notif.id)) > 0:
    #         return FriendInvitationView.notif_react_action(FriendInvitation.objects.get(pk=notif.id))
    #     if len(EventInvitation.objects.filter(pk=notif.id)) > 0:
    #         return EventInvitationView.notif_react_action(EventInvitationView.objects.get(pk=notif.id))
    #     if len(GameLaunching.objects.filter(pk=notif.id)) > 0:
    #         return GameLaunchingView.notif_react_action(GameLaunching.objects.get(pk=notif.id))
    #     return format_html(': )')
    
    # @staticmethod
    # def notif_actions(notif, as_p=False):
    #     return html_utils.html_list_join([NotificationsView.notif_is_read_action(notif),
    #                                  NotificationsView.notif_delete_action(notif),
    #                                   NotificationsView.notif_react_action(notif),], as_p=as_p)
        

    
        
    
class FriendInvitationView(NotificationsView):
    @staticmethod
    def notif_react_action(notif : FriendInvitation):
        return html_utils.same_arg_redir_list(redirs={
            'relationship:accept_friend_request' : 'accept' ,
            'relationship:deny_friend_request' : 'deny' ,
        }, args=[notif.relation.from_user.id], sep= ' | ')

        
class EventInvitationView(NotificationsView):
    @staticmethod
    def notif_react_action(notif : EventInvitation):
        return ""
        return html_utils.same_arg_redir_list(redirs={
            'games:join_game_players' : 'accept' ,
            # 'games:deny_friend_request' : 'deny' ,
        }, args=[notif.game.id, notif.user.id], sep= ' | ')

        
class GameLaunchingView(NotificationsView):
    @staticmethod
    def notif_react_action(notif : GameLaunching):
        return ""

        