from django.shortcuts import render
from accounts.models import User
# Create your views here.
app_name = 'relationship'

def index(request):
    context = {"objects" : User.objects.all(),
               "attribut" : "username",
               "show_url" : f"accounts:profile_page"}
    return render(request, f'{app_name}/index.html', context)

def friend_request(request):
    return render(request, f'{app_name}/friend_request.html', {})