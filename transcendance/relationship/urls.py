from django.urls import path
from . import views
# from . import model_view

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.relation_list, name='all'),
    path('detail/<int:pk>', views.detail, name='detail'),
    
    path('game_invite_players/<int:game>', views.game_invite_view, name='game_invite_players'),
    
    #actions
    path('send_friend_request/<int:pk>', views.to_request, name='send_friend_request'),
    path('accept_friend_request/<int:pk>', views.to_friend, name='accept_friend_request'),
    path('block_user/<int:pk>', views.to_block, name='block_user'),    
    path('unsend_friend_request/<int:pk>', views.to_neutral, name='unsend_friend_request'),
    path('deny_friend_request/<int:pk>', views.to_neutral, name='deny_friend_request'),
    path('unfriend_user/<int:pk>', views.to_neutral, name='unfriend_user'),
    path('unblock_user/<int:pk>', views.to_neutral, name='unblock_user'),

]