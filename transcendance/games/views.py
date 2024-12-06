from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.utils import get_context, redir_to, redir_to_index
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import UpdateView
from .models import Game
# Create your views here.

def index(request):
    return render(request, f'games/index.html', {})

def create_game(request):
    game = Game(user=request.user)
    game.save()
    return redirect('games:settings', game.id)
    

class TodoView(RedirectView):
    pattern_name = 'games:index'

    

class SettingsView(UpdateView):
    #is public
    #launch
    #invite/uninvite players
    model = Game
    fields = [ 'players', 'is_public' ]
    template_name = 'utils/form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        
        # new_game = Game.objects.create(admin=admin, is_public=form.cleaned_data['is_public'])
        # return redir_to_index("games")
        return super().form_valid(form)

class GameView(TemplateView):
    template_name = 'games/game.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
