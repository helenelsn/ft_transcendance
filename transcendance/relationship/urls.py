from django.urls import path
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),
    # path('tournaments/', views.tournaments, name='tournaments'),
    # path('create/', views.create_tournament, name='create_tournament'),
    # path('<tournament_name>', views.show_tournament, name='show_tournament'),
]