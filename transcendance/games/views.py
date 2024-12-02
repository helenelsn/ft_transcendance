from django.shortcuts import render, redirect
from common.utils import get_context
app_name = 'games'
# Create your views here.

def index(request):
    return render(request, f'{app_name}/index.html', get_context(app_name, ))

def redir_to(name):
    return redirect(f'{app_name}:{name}')

def redir_to_index():
    return redir_to('index')


def game(request):
    return render(request, f'{app_name}/game.html', get_context(app_name, ))
    
def settings(request):
    return redir_to('game')
    return render(request, f'{app_name}/index.html')

def lose(request, game_id):
    return redir_to_index()

def win(request, game_id):
    return redir_to_index()