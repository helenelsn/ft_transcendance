from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.index, name='index'),
    path('show_notif/<int:notif_id>', views.show_notif, name='show_notif'),
    
]