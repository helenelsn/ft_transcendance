from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament
from .forms import TournamentForm
from common.utils import get_context, get_form_context, get_table_with_optional_action_context, get_table_context

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
    context = {"tournament" : get_object_or_404(Tournament,  name=tournament_name)}
    return render(request, f'{app_name}/tournament.html', get_context(app_name, context))


def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{app_name}:index")
    else:
        form = TournamentForm()
    return render(request, f'{app_name}/create_tournament.html', get_form_context(app_name, form))