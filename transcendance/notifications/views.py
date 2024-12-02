from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context
from .models import *
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index

app_name = 'notifications'

# Create your views here.
def index(request):
    context = get_action_table_context(
        app_name=app_name,
        objects=Notification.objects.all(),
        field='message',
        url_to_redir='accounts:profile_page',
        actions={'mark as read' : f'relationship:send_friend_request', 'delete' : f'relationship:block_user'},
    ) 
    print(f'{app_name}/index.html')
    return render(request, f'{app_name}/notification_table.html',context )

@login_required
def show_notif(request, notif_id):
    notif = get_object_or_404(Notification.objects.filter(pk=notif_id).filter(user=request.user))
    print(f'---------------------{notif}')
    return redir_to_index(app_name)
    