from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from .models import Event, models, User, EventInvitation
from common.views import ActionModelView, BasicModelView
from common.views import BaseAppView, RedirDict
from relationship.model_view import RelationAppView

class EventAppView(BaseAppView):
    app_name='event'
    
    @property
    def register_viewname(self):
        return self.get_viewname('register')
    
    @property
    def unregister_viewname(self):
        return self.get_viewname('unregister')
    
    @property
    def delete_viewname(self):
        return self.get_viewname('delete')

class EventView(ActionModelView):
    app_view=EventAppView()
    
    
    def __init__(self, object):
        if isinstance(object, int):
            object = Event.objects.get(pk=object)
        super().__init__(object)
        if self.object is None:
            raise Exception("object is none after eventview init")
    
    @property
    def register_url(self) -> str:
        return self.reverse_objectid(self.app_view.register_viewname)
    
    @property
    def unregister_url(self) -> str:
        return self.reverse_objectid(self.app_view.unregister_viewname)
    
    @property
    def delete_url(self) -> str:
        return self.reverse_objectid(self.app_view.delete_viewname)

    @staticmethod
    def create(user : User):
        object = Event(owner=user)
        object.register_player(user.id)
        object.save()
        return EventView(object).settings_view()
    
    #actions
    def delete(self, user : User):
        if self.object.user_is_owner(user.id): 
            Event.objects.delete(self.object)
        return self.index_view()
    
    def register_player(self, user : User):
        self.object.register_player(user)
        return self.detail_view()
    
    def unregister_player(self, user: User):
        self.object.remove_player(user.id)
        return self.detail_view()
    
    def invite_player(self, user_pk : int):
        user = User.objects.get(pk=user_pk)
        EventInvitation().create(user=user, event=self.object)
        return self.detail_view()
    
    #overriding actions
    def get_user_actions_on_obj(self, user : User) -> RedirDict:
        actions = RedirDict()
        if self.object.over: 
            return actions #raise?
        if self.object.user_registerd(user):
            self.add_object_actions(actions='unregister', d=actions)
        elif self.object.joinable(user):
            self.add_object_actions(actions='register', d=actions)
        # if not self.object.is_full and (self.object.user_is_owner(user) or self.object.user_registerd(user)):
        #     RelationAppView.get_invite_url(self.object)
            
        if self.object.user_is_owner(user):
            self.add_object_actions(actions='delete', d=actions)
        return actions

