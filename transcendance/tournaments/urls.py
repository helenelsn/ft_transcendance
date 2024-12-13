from django.urls import path
from . import views

app_name = "tournaments"

urlpatterns = [
    path('', views.create_tournament, name='index'),
    path('create/', views.create_tournament, name='create_tournament'),
    path('settings/<int:pk>', views.TournamentSettingsView.as_view(), name='tournament_settings'),
    path('tournament_detail/<int:pk>', views.TournamentDetailView.as_view(), name='tournament_detail'),
    path('<tournament_name>', views.show_tournament, name='show_tournament'),
]