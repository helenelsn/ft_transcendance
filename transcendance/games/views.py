from django.shortcuts import render
from common.utils import get_context, redir_to, redir_to_index
from django.views.generic.base import RedirectView, TemplateView

# Create your views here.

def index(request):
    return render(request, f'games/index.html', {})

class TodoView(RedirectView):
    pattern_name = 'games:index'

class SettingsView(RedirectView):
    pattern_name = 'games:game'

class GameView(TemplateView):
    template_name = 'games/game.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
