from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ProfileChangeForms, RelationshipForm
from django.contrib.auth.decorators import login_required

# Create your views here.

app_name = "accounts"
home = f'{app_name}/index.html'

def index(request):
    return render(request, home, {})
    # return render(request, "common/g_base.html", {})

def back_to_home():
    return redirect(f'{app_name}:index')

def login_user(request):
    if request.method == 'POST':
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

@login_required
def edit_profile(request):
    
    # if not request.user.is_authenticated:
    #     return redirect(f'{app_name}:register')
    return render(request, f'{app_name}/edit_profile.html', {"forms": ProfileChangeForms(request).to_set()})

@login_required
def handle_relationship(request):
    if request.method == 'POST':
        form = RelationshipForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        form = RelationshipForm(instance=request.user.profile)
    return render(request, f'{app_name}/relationship.html' ,{"forms" :{ form}})


def remove_relationship(request, user : int, other: int):
    return redirect(f'{app_name}:relationship')
    pass