from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('homepage/<username>', views.show_profile, name='homepage'),
    path('edit/', views.edit_profile, name='edit'),
    # path('<tournament_name>', views.show_tournament, name='show_tournament')
    path('relationship/', views.handle_relationship, name='relationship'),
    path('relationship/delete_friend/<int:user>/int<other>', views.remove_relationship, name='relationship'),
]
