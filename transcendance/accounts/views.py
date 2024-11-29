from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

app_name = "accounts"
home = f'{app_name}/index.html'

def index(request):
    return render(request, home, {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'{app_name}:index')
        else:
            messages.info(request, "Username or password incorret")

    form = AuthenticationForm()
    return render(request, f"{app_name}/login.html", {"form" : form})


def logout_user(request):
    logout(request)
    return redirect(f'{app_name}:index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'{app_name}:index')
        else:
            messages.info(request, "Username or password incorret")

    form = UserCreationForm()
    return render(request, f"{app_name}/register.html", {"form" : form})