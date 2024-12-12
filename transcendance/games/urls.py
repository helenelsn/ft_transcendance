from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.further_games_list_view, name='index'),
    path('history/', views.game_history_list_view, name='game_history'),
    path('game_detail/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
    
    path('create_game/', views.create_game, name='create_game'),
    path('launch_game/<int:pk>', views.launch_game, name='launch_game'),
    path('game/<int:pk>', views.game, name='game'),
    # path('play_game/<int:pk>', views.TmpGameView.as_view(), name='play_game'),
    path('delete_game/<int:pk>', views.delete_game, name='delete_game'),
    path('settings/<int:pk>', views.SettingsView.as_view(), name='settings'),
    
    #actions
    path('invite_player/<int:pk>/<int:player_pk>', views.invite_player, name='invite_player'),
    path('join_game_players/<int:pk>/<int:player_pk>', views.join_game_players, name='join_game_players'),
    path('unjoin_game_players/<int:pk>/<int:player_pk>', views.unjoin_game_players, name='unjoin_game_players'),
  
    
]
