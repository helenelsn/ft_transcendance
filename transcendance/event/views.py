from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from .models import Event, models, User, EventInvitation

class BasicModelView(ABC):
    #abstarct view for object with name, detail, setting and index view
    def __init__(self, object : models.Model, app_name='app_name'):
        self.object : models.Model = object
        self.app_name = app_name
        
    def linked_name(self, url):
        return html_utils.format_hyperlink(url, display=self.object.name)
    
    @property
    def detail_linked_name(self):
        return self.linked_name(self.absolute_url)
    
    @property
    def settings_url(self):
        return reverse(f"{self.app_name}:settings", kwargs={"pk": self.pk})
    
    @property
    def absolute_url(self):
        return self.object.get_absolute_url()
    
    def detail_view(self):
        return redirect(self.absolute_url)
    
    def settings_view(self):
        return redirect(self.settings_url)
        
    def index_view(self):
        return redirect(f'{self.app_name}:index')


#parent view for user related and action views?

# Create your views here.
class EventView(BasicModelView):
    def __init__(self, object, app_name='games'):
        self.app_name = app_name
        if isinstance(object, int):
            object = Event.objects.get(pk=object)
        super(BasicModelView, self).__init__(object, app_name)
        self.object = object
        if self.object is None:
            raise Exception("object is none after eventview init")
        
    @staticmethod
    def create(user : User):
        object = Event(owner=user)
        object.register_player(user.id)
        object.save()
        return EventView(object).settings_view()
    
    def delete(self):
        Event.objects.delete(self.object)
        return self.index_view()
    
    def register_player(self, user : User):
        self.object.register_player(user.id)
        return self.detail_view()
    
    def unregister_player(self, user_pk):
        self.object.remove_player(user_pk)
        return self.detail_view()
    
    def invite_player(self, user_pk):
        user = User.objects.get(pk=user_pk)
        EventInvitation().create(user=user, event=self.object)
        return redirect(self.detail_view())
    
@login_required
def create_event(request):
    return EventView.create(request.user)

@login_required
def register_player(request, pk):
    return EventView(object=pk).register_player(request.user)

@login_required
def unregister_event(request, pk, player_pk):
    return EventView(pk).unregister_player(player_pk)

@login_required 
def delete_event(request, pk):
    return EventView(pk).delete()

@login_required
def invite_player(request, pk, player_pk):
    return EventView(pk).invite_player(player_pk)

