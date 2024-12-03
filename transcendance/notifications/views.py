from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context, get_context
from .models import *
from relationship.models import FriendInvitation
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any


from django.views.generic import ListView, DetailView
app_name = 'notifications'

class NotificationsView():
    model = Notification
    
    @staticmethod
    def update(request, notif, att : str, val : Any):
        n : Notification = get_object_or_404(request.user.notification_set.filter(pk = notif))
        setattr(n, att, val)
        n.save()

    @login_required
    def read(request, pk):
        NotificationsView.update(request, pk, 'is_read', True)
        return redir_to(app_name, 'all')
        
    @login_required
    def unread(request, pk):
        NotificationsView.update(request, pk, 'is_read', False)
        return redir_to(app_name, 'all')

    @login_required
    def delete(request, pk):
        Notification.delete(pk)
        return redir_to(app_name, 'all')

    @login_required
    def read_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            NotificationsView.update(request, notif.id, 'is_read', True)
        return redir_to(app_name, 'all')
            
        
    @login_required
    def unread_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            NotificationsView.update(request, notif.id, 'is_read', False)
        return redir_to(app_name, 'all')
        
    @login_required
    def delete_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            Notification.delete(notif=notif.id)
        return redir_to(app_name, 'all')

    @staticmethod
    def get_generic_actions_names():
        return ["(un)read", "delete"]

    @staticmethod
    def get_generic_actions(notif):
        n :Notification = Notification.objects.get(pk = notif)
        if n.is_read:
            actions = {'unread' : 'notifications:unread_notif'}
        else: 
            actions = {'read' : 'notifications:read_notif'}
        actions.update({'delete' : 'notifications:delete_notif'})
        return actions

    @staticmethod
    def get_global_actions():
        return {
            'delete all' : 'notifications:delete_all_notif',
            'read all' : 'notifications:read_all_notif',
            'unread all' : 'notifications:unread_all_notif',
            'show all':'notifications:all',
            'hide read': 'notifications:index'
        }
        
class NotificationsDetailsView(NotificationsView, DetailView):
    template_name = f'{app_name}/notification_detail.html'
    

class NotificationsListView(NotificationsView, ListView):
    template_name = f'{app_name}/notification_table.html'
    def get_queryset(self) :
        queryset = self.model.objects.order_by('-timestamp').filter(user=self.request.user)
        return queryset
    

class UnreadsNotificationsListView(NotificationsListView):
    template_name = f'{app_name}/notification_table.html'
    def get_queryset(self) :
        queryset = self.model.objects.order_by('timestamp').filter(user=self.request.user).filter(is_read=False)
        return queryset



    