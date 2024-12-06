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
from .filters import TournamentFilter
from .tables import TournamentTable

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


def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{app_name}:index")
    else:
        form = TournamentForm()
    return render(request, f'{app_name}/create_tournament.html', get_form_context(app_name, form))

class TournamentListView(SingleTableMixin, FilterView):
    table_class = TournamentTable
    model = Tournament
    template_name = "notifications/notification_list.html"
    filterset_class = TournamentFilter