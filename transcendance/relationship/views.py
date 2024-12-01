from django.shortcuts import render

# Create your views here.
app_name = 'relationship'

def index(request):
    return render(request, f'{app_name}/index.html', {})