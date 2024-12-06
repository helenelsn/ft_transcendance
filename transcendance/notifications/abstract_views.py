from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context, get_context
from relationship.models import FriendInvitation
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any
from .models import Notification
from common.templatetags import html_utils
from django.utils.html import format_html

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
        return redir_to_index(app_name)
        
    @login_required
    def unread(request, pk):
        NotificationsView.update(request, pk, 'is_read', False)
        return redir_to_index(app_name)

    @login_required
    def delete(request, pk):
        Notification.delete(pk)
        return redir_to_index(app_name)

    @login_required
    def read_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            NotificationsView.update(request, notif.id, 'is_read', True)
        return redir_to_index(app_name)
            
        
    @login_required
    def unread_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            NotificationsView.update(request, notif.id, 'is_read', False)
        return redir_to_index(app_name)
        
    @login_required
    def delete_all(request):
        for notif in request.user.notification_set.all().filter(user=request.user):
            Notification.delete(notif=notif.id)
        return redir_to_index(app_name)

    @staticmethod
    def all_notif_managment_actions():
        return html_utils.simple_redir_list(redirs={
            'notifications:delete_all_notif' : 'delete all' ,
            'notifications:read_all_notif' : 'read all' ,
            'notifications:unread_all_notif' : 'unread all' ,
        }, as_p=True)
        
    @staticmethod
    def notif_is_read_action(notif):
        actions = [
            ('read_notif' , 'mark read'),
            ('unread_notif' , 'mark unread')
        ]
        args=[notif.id]
        return html_utils.a_hyperlink(redir=f'notifications:{actions[notif.is_read][0]}', display=actions[notif.is_read][1], args=args)
    
    @staticmethod
    def notif_delete_action(notif):
        return html_utils.a_hyperlink(redir=f'notifications:delete_notif', display='delete', args=[notif.id])
    
    @staticmethod
    def notif_react_action(notif):
        if len(FriendInvitation.objects.filter(pk=notif.id)) > 0:
            return FriendInvitationView.notif_react_action(FriendInvitation.objects.get(pk=notif.id))
        return format_html(': )')
    
    @staticmethod
    def notif_actions(notif, as_p=False):
        return html_utils.html_list_join([NotificationsView.notif_is_read_action(notif),
                                     NotificationsView.notif_delete_action(notif),
                                      NotificationsView.notif_react_action(notif),], as_p=as_p)
        

    
        
    
class FriendInvitationView(NotificationsView):
    @staticmethod
    def notif_react_action(notif):
        return html_utils.same_arg_redir_list(redirs={
            'relationship:accept_friend_request' : 'accept' ,
            'relationship:deny_friend_request' : 'deny' ,
        }, args=[notif.relation.from_user.username], sep= ' | ')