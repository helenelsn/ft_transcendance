from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from .models import Event, models, User, EventInvitation
from common.views import ActionModelView


class EventView(ActionModelView):
    app_name='event'
    
    def __init__(self, object):
        if isinstance(object, int):
            object = Event.objects.get(pk=object)
        super().__init__(object)
        # self.object : Event = object
        if self.object is None:
            raise Exception("object is none after eventview init")
    
    @property
    def register_url(self) -> str:
        return self.reverse_objectid('event:register')
    
    @property
    def unregister_url(self) -> str:
        return self.reverse_objectid('event:unregister')
    
    @property
    def delete_url(self) -> str:
        return self.reverse_objectid('event:delete')

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
        return redirect(self.detail_view())
    
    #overriding actions
    def get_actions(self, user : User) -> dict:
        actions = {}
        if self.object.over: 
            return actions #raise?
        if self.object.user_registerd(user):
            actions[self.unregister_url] = 'unregister'
        elif self.object.joinable(user):
            actions[self.register_url] = 'register'
        if not self.object.is_full and (self.object.user_is_owner(user) or self.object.user_registerd(user)):
            actions[reverse('relationship:game_invite_players', args=[self.object.pk])] = 'invite players'
        if self.object.user_is_owner(user):
            actions[self.delete_url] = 'delete'
        return actions

