from django.urls import path
from . import views, abstract_views

app_name = "games"

urlpatterns = [
    # path('', views.further_games_list_view, name='index'),
    # path('history/', views.game_history_list_view, name='game_history'),
    # path('open_games/', views.open_games, name='open_games'),
    path('game_detail/<int:pk>', views.GameDetailView.as_view(), name='detail'),
    
    # path('create_game/', abstract_views.GameView.create, name='create_game'),
    # path('launch_game/<int:pk>', abstract_views.GameView.launch_game, name='launch_game'),
    # path('game/<int:pk>', views.game, name='game'),
    # # path('play_game/<int:pk>', views.TmpGameView.as_view(), name='play_game'),
    # path('delete_game/<int:pk>', abstract_views.GameView.delete_game, name='delete_game'),
    # path('settings/<int:pk>', views.GameSettingsView.as_view(), name='settings'),
    
    # #actions
    # path('invite_player/<int:pk>/<int:player_pk>', abstract_views.GameView.invite_player, name='invite_player'),
    # path('join_game_players/<int:pk>/<int:player_pk>', abstract_views.GameView.join_players, name='join_game_players'),
    # path('unjoin_game_players/<int:pk>/<int:player_pk>', abstract_views.GameView.unjoin_game_players, name='unjoin_game_players'),
  
    
]
