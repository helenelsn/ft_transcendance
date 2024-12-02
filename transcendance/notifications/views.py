from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context
from .models import *
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index

app_name = 'notifications'

@login_required
def index(request):
    context = get_action_table_context(
        app_name=app_name,
        objects=Notification.get_user_unreads_notifs(request.user),
        field='id',
        url_to_redir='notifications:show_notif',
        actions={'mark as read' : f'notifications:read_notif', 'delete' : f'notifications:delete_notif'},
        d={
            'endredir':'all_notif',
            'endredir_mess': 'show all',
        },
    ) 
    print(f'{app_name}/index.html')
    return render(request, f'{app_name}/index.html',context )

@login_required
def all_notif(request):
    context = get_action_table_context(
        app_name=app_name,
        objects=Notification.get_user_notifs(request.user),
        field='id',
        url_to_redir='notifications:show_notif',
        actions={'mark as read' : f'notifications:read_notif', 'delete' : f'notifications:delete_notif'},
        d= {
            'endredir':'index',
            'endredir_mess': 'mask read',
        },
    ) 
    print(f'{app_name}/index.html')
    return render(request, f'{app_name}/index.html',context )


@login_required
def show_notif(request, notif_id):
    notif = get_object_or_404(Notification.filter_notif(notif_id, request.user))
    print(f'---------------------{notif}')
    return redir_to_index(app_name)

@login_required
def read_notif(request, notif_id):
    notif = get_object_or_404(Notification.filter_notif(notif_id, request.user))
    notif.is_read = True
    notif.save()
    return redir_to_index(app_name)
    
@login_required
def unread_notif(request, notif_id):
    notif = get_object_or_404(Notification.filter_notif(notif_id, request.user))
    notif.is_read = False
    notif.save()
    return redir_to_index(app_name)

@login_required
def delete_notif(request, notif_id):
    Notification.filter_notif(notif_id, request.user).delete()
    return redir_to_index(app_name)
    