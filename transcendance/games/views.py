from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from common.utils import get_context, redir_to, redir_to_index
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Game, GameInvitation
from .filters import GamesFilter
from .tables import GamesTable
from accounts.models import User


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

def invite_player(request, pk, player_pk):
    game = Game.objects.get(pk=pk)
    user = User.objects.get(pk=player_pk)
    message = f'user {request.user.username} invited you to join game {game.name}'
    
    notif = GameInvitation(user=user, game=game, message=message)
    notif.save()
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
