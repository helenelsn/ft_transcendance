from django.urls import path
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:relation_id>/<username>', views.update_relation, name='send_friend_request'),
    path('send_friend_request/<username>', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<username>', views.accept_friend_request, name='accept_friend_request'),
    path('delete_friend/<username>', views.delete_friend, name='delete_friend'),
    path('unblock_user/<username>', views.unblock_user, name='unblock_user'),
    path('block_user/<username>', views.block_user, name='block_user'),
]