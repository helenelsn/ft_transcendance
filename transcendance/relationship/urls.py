from django.urls import path
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),
    path('friend_request/<username>', views.friend_request, name='friend_request'),
    path('delete_friend/<username>', views.delete_friend, name='delete_friend'),
    path('all_user/', views.all_user, name='all_user'),
    # path('tournaments/', views.tournaments, name='tournaments'),
    # path('create/', views.create_tournament, name='create_tournament'),
    # path('<tournament_name>', views.show_tournament, name='show_tournament'),
]