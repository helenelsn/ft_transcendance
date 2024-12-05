from django.urls import path
from . import views

app_name = "tournaments"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_tournament, name='create_tournament'),
    path('<tournament_name>', views.show_tournament, name='show_tournament'),
]