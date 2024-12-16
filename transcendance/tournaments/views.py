from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament
from .forms import TournamentForm
from common.utils import get_context, get_form_context, get_optional_action_table_context, get_table_context
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .filters import TournamentFilter
from .tables import TournamentTable
from django.urls import reverse
from tournaments.abstract_views import TournamentView

app_name = 'tournaments'

def index(request):
    context = get_table_context(
        app_name=app_name,
        objects=Tournament.objects.all(),
        field='name',
        url_to_redir=f"{app_name}:show_tournament",
    )
    return render(request, f'{app_name}/index.html', context)



def show_tournament(request, tournament_name):
    tournament = get_object_or_404(Tournament,  name=tournament_name)
    context = get_table_context(app_name=app_name, objects=tournament.players.all(), url_to_redir='accounts:profil_detail', field='username')
    return render(request, f'{app_name}/tournament.html', context)




# @login_required
class TournamentSettingsView(UpdateView):
    model = Tournament
    fields = ['name', 'public', 'number_players']
    template_name = 'utils/form.html'
    
class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'tournaments/tournament_detail.html'
    
@login_required
def create_tournament(request):
    t = Tournament.create_tournament(request.user)
    return redirect(TournamentView(t).get_edit_url())
    
class TournamentListView(SingleTableMixin, FilterView):
    table_class = TournamentTable
    model = Tournament
    template_name = "tournaments/tournament_list.html"
    filterset_class = TournamentFilter