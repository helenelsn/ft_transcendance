from django.urls import path
from . import views
app_name = "event"
urlpatterns = [
    path('create_event/', views.create_event, name='create'), #=>del
    path('event_detail/<int:pk>', views.event_detail, name='detail'),
    #settings
    path('register_event/<int:pk>', views.register_event, name='register'),
    path('unregister_event/<int:pk>', views.unregister_event, name='unregister'),
    path('delete_event/<int:pk>', views.delete_event, name='delete'),
    path('invite_to_event/<int:pk>/<int:player_pk>', views.invite_to_event, name='invite'),
    
]
