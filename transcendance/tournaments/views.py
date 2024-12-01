from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament
from .forms import TournamentForm

app_name = 'tournaments'

def index(request):
    context = {"objects" : Tournament.objects.all(),
               "field" : "name",
               "redir" : f"{app_name}:show_tournament"}
    
    return render(request, f'{app_name}/index.html', context)



def show_tournament(request, tournament_name):
    context = {"tournament" : get_object_or_404(Tournament,  name=tournament_name)}
    return render(request, f'{app_name}/tournament.html', context)


def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{app_name}:index")
    else:
        form = TournamentForm()
    return render(request, f'{app_name}/create_tournament.html', {"forms": {form}})