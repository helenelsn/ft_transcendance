from django.urls import path
from . import views
from django.views.generic import TemplateView
# from django.conf.urls import url
app_name = 'notifications'


urlpatterns = [
    path('', views.UnreadsNotificationsListView.as_view(), name='index'),
    path('all/', views.NotificationsListView.as_view(), name='all'),
    path('show_notif/(?P<pk>\d+)', views.NotificationsDetailsView.as_view(), name='show_notif'),
    
    #act on notif 
    path('read_notif/(?P<pk>\d+)>', views.NotificationsView.read, name='read_notif'),
    path('unread_notif/(?P<pk>\d+)', views.NotificationsView.unread, name='unread_notif'),
    path('delete_notif/(?P<pk>\d+)', views.NotificationsView.delete, name='delete_notif'),
    
    path('read_all_notif/', views.NotificationsView.read_all, name='read_all_notif'),
    path('unread_all_notif/', views.NotificationsView.unread_all, name='unread_all_notif'),
    path('delete_all_notif/', views.NotificationsView.delete_all, name='delete_all_notif'),
    
]