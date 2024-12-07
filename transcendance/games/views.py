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


def index(request):
    return render(request, f'games/index.html', {})

def create_game(request):
    game = Game(user=request.user)
    game.save()
    return redirect('games:settings', game.id)
    
def join_game_players(request, pk, player):
    game = Game.objects.get(pk=pk)
    game.players.add(Profile.objects.filter(user=player).get())
    game.save()
    return redirect(game.get_absolute_url())
    
def invite_player_in_game(request, pk, player):
    game = Game.objects.get(pk=pk)
    game.players.add(Profile.objects.filter(user=player).get())
    game.save()
    return redirect('relationship:game_invite_players', game.id)
    
    
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
    
class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    

# class RelationListView(SingleTableMixin, ListView):
#     table_class = GamesTable
#     model = Game
#     template_name = "relationship/relation_list.html"


def games_list_view(request):
    f = GamesFilter(request.GET, request=request, queryset=Game.objects.all())
    table = GamesTable(data=f.qs, request=request)
    
    return render(request, 'games/game_list.html', {'filter': f, 'table':table})
