from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import Relation, FRIEND, NEUTRAL, BLOCKED, REQUEST
# Create your views here.
app_name = 'relationship'

def index(request):
    context = {
        'objects': User.objects.all(),
        'field': 'username',
        'redir': 'accounts:profile_page',
        'action_cond': request.user.is_authenticated,
        'actions':{'friend' : f'relationship:send_friend_request', 'block' : f'relationship:block_user'},
    }
    return render(request, f'{app_name}/all_user.html', context)

# def all_user(request):
#     return render(request, f'{app_name}/all_user.html', context)
    
@login_required
def update_relation(request, relation_id : int, username : str, ):
    to_user = get_object_or_404(User, username=username).profile
    Relation().update_relation(from_user=request.user.profile, to_user=to_user, type=relation_id)
    return redirect(f'{app_name}:index')
 

@login_required
def send_friend_request(request, username):
    return update_relation(request, REQUEST, username)
    Relation().update_relation(from_user=request.user.profile, to_user=get_object_or_404(User, username=username).profile, relation=2).create_relation()
    return redirect(f'{app_name}:index')

@login_required
def accept_friend_request(request, username):
    return update_relation(request, FRIEND, username)

@login_required
def delete_friend(request, username):
    return update_relation(request, NEUTRAL, username)
    Relation(from_user=request.user.profile, to_user=get_object_or_404(User, username=username).profile, relation=3).create_relation()
    return render(request, f'{app_name}/index.html', {})

@login_required
def unblock_user(request, username):
    return update_relation(request, NEUTRAL, username)

@login_required
def block_user(request, username):
    return update_relation(request, BLOCKED, username)
