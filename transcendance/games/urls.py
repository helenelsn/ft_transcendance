from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('settings/', views.settings, name='settings'),
    path('lose/<int:game_id>', views.lose, name='lose'),
    path('win/<int:game_id>', views.win, name='win'),
]
