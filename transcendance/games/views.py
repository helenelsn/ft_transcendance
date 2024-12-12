from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse
from django.forms import Form
from django import forms
from django.views.generic.edit import UpdateView
from common.utils import redir_to, redir_to_index
from .models import Game, GameInvitation, GameLaunching, GameHistory
from .filters import FurtherGamesFilter, GameHistoryFilter
from .tables import GamesTable, GamesHistoryTable
from accounts.models import User


def create_game(request):
    game = Game(left_player=request.user)
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

def launch_game(request, pk):
    game = Game.objects.get(pk=pk)
    message = f'Game {game.name} beginning'
    user = game.left_player
    notif = GameLaunching(user=user, game=game, message=message)
    notif.save()
    user = game.right_player
    notif = GameLaunching(user=user, game=game, message=message)
    notif.save()
    
    history = GameHistory.objects.get(game=game)
    print('redirecting')
    return redirect(reverse("games:game", args=[history.pk]))
    
def game(request, pk):
    history = GameHistory.objects.get(pk=pk)
    if history.over:
        return redirect(Game.objects.get(pk=history.game.id))
    
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            history.over = True
            score = abs(int(form.data['score']))
            if history.game.right_player == request.user:
                history.right_score = score
            else:
                history.left_score = score
            # if history.right_score > 0 and history.left_score > 0:
            #     history.over = True
            history.save()
            return redirect(Game.objects.get(pk=history.game.pk))
        
    score = forms.IntegerField(label='score')
    f = Form()
    f.fields.update({'score' : score})
    return render(request=request, template_name='games/game.html', context={'form':f})
    


class SettingsView(UpdateView):
    model = Game
    fields = ['name', 'is_public' ]
    template_name = 'utils/form.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        
        # new_game = Game.objects.create(admin=admin, is_public=form.cleaned_data['is_public'])
        # return redir_to_index("games")
        return super().form_valid(form)

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    
def further_games_list_view(request):
    f = FurtherGamesFilter(request.GET, request=request, queryset=Game.objects.all())
    table = GamesTable(data=f.qs, request=request)
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})


def game_history_list_view(request):
    f = GameHistoryFilter(request.GET, request=request, queryset=GameHistory.objects.all())
    table = GamesHistoryTable(data=f.qs, request=request)
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})

