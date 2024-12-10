from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.games_list_view, name='index'),
    path('game_detail/<int:pk>', views.GameDetailView.as_view(), name='game_detail'),
    
    path('create_game/', views.create_game, name='create_game'),
    path('delete_game/<int:pk>', views.delete_game, name='delete_game'),
    path('settings/<int:pk>', views.SettingsView.as_view(), name='settings'),
    
    #actions
    path('join_game_players/<int:pk>/<int:player_pk>', views.join_game_players, name='join_game_players'),
    path('unjoin_game_players/<int:pk>/<int:player_pk>', views.unjoin_game_players, name='unjoin_game_players'),
    
    path('lose/', views.TodoView.as_view(), name='lose'),
    path('win/', views.TodoView.as_view(), name='win'),
    
]
