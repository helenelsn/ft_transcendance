from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_notif/', views.all_notif, name='all_notif'),
    path('show_notif/<int:notif_id>', views.show_notif, name='show_notif'),
    path('read_notif/<int:notif_id>', views.read_notif, name='read_notif'),
    path('unread_notif/<int:notif_id>', views.unread_notif, name='unread_notif'),
    path('delete_notif/<int:notif_id>', views.delete_notif, name='delete_notif'),
    
]