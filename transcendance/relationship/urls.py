from django.urls import path
from . import views

app_name = 'relationship'

urlpatterns = [
    path('', views.index, name='index'),

    path('detail/', views.RelationListView.as_view(), name='detail'),
    # path('detail/<rel_key>', views.render_relation_table, name='detail'),
    
    
    path('send_friend_request/<username>', views.RelationView.send_friend_request, name='send_friend_request'),
    path('unsend_friend_request/<username>', views.RelationView.unsend_friend_request, name='unsend_friend_request'),
    
    path('accept_friend_request/<username>', views.RelationView.accept_friend_request, name='accept_friend_request'),
    path('deny_friend_request/<username>', views.RelationView.deny_friend_request, name='deny_friend_request'),
    path('unfriend_user/<username>', views.RelationView.unfriend_unser, name='unfriend_user'),
    path('delete_friend/<username>', views.RelationView.delete_friend, name='delete_friend'),
    path('unblock_user/<username>', views.RelationView.unblock_user, name='unblock_user'),
    path('block_user/<username>', views.RelationView.block_user, name='block_user'),

]