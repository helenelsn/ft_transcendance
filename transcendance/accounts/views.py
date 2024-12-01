from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import ProfileChangeForm
from .models import User, Profile
# Create your views here.

app_name = "accounts"
home = f'{app_name}/index.html'

def index(request):
    # for i in range(100):
    #     User.objects.create_user(username=f'user{i}',
    #                              password=f'ViveLeVent{i}')
        
    if request.user.is_authenticated:
        return redirect(f'{app_name}:profile_page', request.user.username)
    return render(request, home, {})

def back_to_home():
    return redirect(f'{app_name}:index')

def login_user(request):
    if request.method == 'POST':
        print("username=",f'{request.POST["username"]}', "password=", f'{request.POST["password"]}')
        print(User.objects.get(username=request.POST["username"]).password)
        user = authenticate(request=request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return back_to_home()
        else:
            messages.info(request, "Username or password incorret")
    form = AuthenticationForm()
    return render(request, f"{app_name}/login.html",  {"forms": {form}})

def logout_user(request):
    logout(request)
    return back_to_home()

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'{app_name}:index')
        else:
            messages.info(request, "Username or password incorret")
    form = UserCreationForm()
    return render(request, f"{app_name}/register.html", {"forms" : {form}})

def show_profile(request, username):
    print(username , request.user.username, request.user.is_authenticated)
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be logged in")
    return render(request, f'{app_name}/profile_page.html', {"profile":User.objects.filter(username=username).get()})
    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileChangeForm(request.POST, instance = Profile.objects.filter(user=request.user).get())
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileChangeForm(instance = Profile.objects.filter(user=request.user).get())
    return render(request, f'{app_name}/edit_profile.html', {"forms": [profile_form]})

