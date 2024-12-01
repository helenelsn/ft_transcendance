from django.shortcuts import render, get_object_or_404
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import Relation
# Create your views here.
app_name = 'relationship'

def index(request):
    return render(request, f'{app_name}/all_user.html', {'all_user' : User.objects.all()})
    # context = {"objects" : User.objects.all(),
    #            "attribut" : "username",
    #            "show_url" : f"accounts:profile_page"}
    # return render(request, f'{app_name}/index.html', context)

def all_user(request):
    return render(request, f'{app_name}/all_user.html', {'all_user' : User.objects.all()})
    
@login_required
def friend_request(request, username):
    #create new relation friend requesr and send notif
    # if Relation.objects.get(myself=username, other=request.u)
    relation = Relation.objects.create(from_user=request.user.profile, to_user=get_object_or_404(User, username=username).profile, relation=2)
    relation.save()
    return render(request, f'{app_name}/friend_request.html', {})

@login_required
def delete_friend(request, username):
    return render(request, f'{app_name}/index.html', {})

