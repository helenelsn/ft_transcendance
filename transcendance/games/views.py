from django.shortcuts import render
from common.utils import get_context, redir_to, redir_to_index
app_name = 'games'
# Create your views here.

def index(request):
    return render(request, f'{app_name}/index.html', get_context(app_name, ))


def game(request):
    return render(request, f'{app_name}/game.html', get_context(app_name, ))
    
def settings(request):
    return redir_to(app_name, 'game')
    return render(request, f'{app_name}/index.html')

def lose(request, game_id):
    return redir_to_index(app_name)

def win(request, game_id):
    return redir_to_index(app_name)