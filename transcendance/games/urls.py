from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.index, name='index'),
    
    path('game/', views.GameView.as_view(), name='game'),
    path('game_detail/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
    path('game_list/', views.games_list_view, name='game_list'),
    
    path('invite_player/<int:pk>/<int:player>', views.invite_player_in_game, name='invite_player'),
    path('join_game_players/<int:pk>/<int:player>', views.join_game_players, name='join_game_players'),
    path('settings/<int:pk>', views.SettingsView.as_view(), name='settings'),
    path('create_game/', views.create_game, name='create'),
    
    path('lose/', views.TodoView.as_view(), name='lose'),
    path('win/', views.TodoView.as_view(), name='win'),
    
]
