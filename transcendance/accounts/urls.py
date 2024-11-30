from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit/', views.edit_profile, name='edit'),
    path('relationship/', views.handle_relationship, name='relationship'),
    # path('<tournament_name>', views.show_tournament, name='show_tournament')
]
