from django.shortcuts import render
import common
app_name = 'games'
# Create your views here.
def index(request):
    return render(request, 'common/index.html', {'title' : "Games"})
