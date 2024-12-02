from django.shortcuts import render, redirect
from .utils import game_context
import common
app_name = 'games'
# Create your views here.

def index(request):
    return render(request, f'{app_name}/index.html', game_context())

def game(request):
    return render(request, f'{app_name}/game.html', game_context())
    
def settings(request):
    return redirect(f'{app_name}:game')
    return render(request, f'{app_name}/index.html')

def lose(request, game_id):
    return redirect(f'{app_name}:index')

def win(request, game_id):
    return redirect(f'{app_name}:index')