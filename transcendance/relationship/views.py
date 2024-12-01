from django.shortcuts import render
from accounts.models import User
# Create your views here.
app_name = 'relationship'

def index(request):
    context = {"objects" : User.objects.all(),
               "attribut" : "username",
               "show_url" : f"accounts:profile_page"}
    return render(request, f'{app_name}/index.html', context)

def all_user(request):
    return render(request, f'{app_name}/all_user.html', {'all_user' : User.objects.all()})
    

def friend_request(request, username):
    return render(request, f'{app_name}/friend_request.html', {})

def delete_friend(request, username):
    return render(request, f'{app_name}/index.html', {})