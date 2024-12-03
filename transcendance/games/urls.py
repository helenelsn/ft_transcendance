from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.index, name='index'),
    
    path('game/', views.GameView.as_view(), name='game'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    
    path('lose/', views.TodoView.as_view(), name='lose'),
    path('win/', views.TodoView.as_view(), name='win'),
]
