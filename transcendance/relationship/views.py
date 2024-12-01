from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import Relation
# Create your views here.
app_name = 'relationship'

def index(request):
    context = {
        'objects': User.objects.all(),
        'field': 'username',
        'redir': 'accounts:profile_page',
    } 
    # 'redir': 'relationship:friend_request',
    # print(f'----------------{context}--------------')
    return render(request, f'{app_name}/all_user.html', context)
    # context = {"objects" : User.objects.all(),
    #            "attribut" : "username",
    #            "show_url" : f"accounts:profile_page"}
    # return render(request, f'{app_name}/index.html', context)

def all_user(request):
    return render(request, f'{app_name}/all_user.html', context)
    
@login_required
def friend_request(request, username):
    Relation(from_user=request.user.profile, to_user=get_object_or_404(User, username=username).profile, relation=2).create_relation()
    return redirect(f'{app_name}:index')

@login_required
def delete_friend(request, username):
    return render(request, f'{app_name}/index.html', {})

