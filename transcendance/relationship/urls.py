from django.urls import path
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),

    path('detail/', views.RelationListView.as_view(), name='detail'),
    path('game_invite_players/<int:game>', views.game_invite_view, name='game_invite_players'),
    
    
    path('send_friend_request/<int:pk>', views.RelationView.send_friend_request, name='send_friend_request'),
    path('unsend_friend_request/<int:pk>', views.RelationView.unsend_friend_request, name='unsend_friend_request'),
    path('accept_friend_request/<int:pk>', views.RelationView.accept_friend_request, name='accept_friend_request'),
    path('deny_friend_request/<int:pk>', views.RelationView.deny_friend_request, name='deny_friend_request'),
    path('unfriend_user/<int:pk>', views.RelationView.unfriend_unser, name='unfriend_user'),
    path('delete_friend/<int:pk>', views.RelationView.delete_friend, name='delete_friend'),
    path('unblock_user/<int:pk>', views.RelationView.unblock_user, name='unblock_user'),
    path('block_user/<int:pk>', views.RelationView.block_user, name='block_user'),

]