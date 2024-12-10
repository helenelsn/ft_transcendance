from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.utils import get_context, redir_to, redir_to_index
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Game
from django_tables2.views import SingleTableMixin
from .filters import GamesFilter
from accounts.models import Profile
from .tables import GamesTable


def create_game(request):
    game = Game(owner=request.user, left_player=request.user)
    game.save()
    return redirect('games:settings', game.id)
    
def delete_game(request, pk):
    Game.objects.filter(pk=pk).delete()
    return redir_to_index('games')
    
def join_game_players(request, pk, player_pk):
    game = Game.objects.get(pk=pk)
    game.add_player(player_pk)
    return redirect(game.get_absolute_url())

def unjoin_game_players(request, pk, player_pk):
    game = Game.objects.get(pk=pk)
    game.remove_player(player_pk)
    return redir_to_index('games')

    
    
class TodoView(RedirectView):
    pattern_name = 'games:index'

class SettingsView(UpdateView):
    model = Game
    fields = [ 'is_public' ]
    template_name = 'utils/form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        
        # new_game = Game.objects.create(admin=admin, is_public=form.cleaned_data['is_public'])
        # return redir_to_index("games")
        return super().form_valid(form)

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    
def games_list_view(request):
    f = GamesFilter(request.GET, request=request, queryset=Game.objects.all())
    table = GamesTable(data=f.qs, request=request)
    
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})
