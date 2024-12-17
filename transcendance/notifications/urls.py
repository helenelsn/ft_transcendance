from django.urls import path
from . import views
from django.views.generic import TemplateView
# from django.conf.urls import url
app_name = 'notifications'


urlpatterns = [
    path('', views.NotificationsListView.as_view(), name='index'),
    path('all/', views.NotificationsListView.as_view(), name='all'),
    path('show_notif/<int:pk>', views.NotificationsDetailsView.as_view(), name='show_notif'),
    
    
    #act on notif 
    path('notif_act/<str:action>/<int:pk>', views.notif_act, name='notif_act'),
    
]