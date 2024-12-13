from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.forms import Form
from django import forms
from django.views.generic.edit import UpdateView
from .models import Game, GameHistory
from .filters import FurtherGamesFilter, GameHistoryFilter, OpenGamesFilter
from .tables import GamesTable, GamesHistoryTable
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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

@login_required
def further_games_list_view(request):
    f = FurtherGamesFilter(request.GET, request=request, queryset=Game.objects.all())
    table = GamesTable(data=f.qs, request=request)
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})


@login_required
def game_history_list_view(request):
    f = GameHistoryFilter(request.GET, request=request, queryset=GameHistory.objects.all())
    table = GamesHistoryTable(data=f.qs, request=request)
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})

    
@login_required
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
            history.save()
            return redirect(Game.objects.get(pk=history.game.pk))
        
    score = forms.IntegerField(label='score')
    f = Form()
    f.fields.update({'score' : score})
    return render(request=request, template_name='games/game.html', context={'form':f})
    

def open_games(request):
    f = OpenGamesFilter(request.GET, request=request, queryset=Game.objects.all())
    table = GamesTable(data=f.qs, request=request)
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})