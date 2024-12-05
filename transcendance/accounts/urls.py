from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.render_user_table, name='all'),
    
    # authentication
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    
    # profil managment
    path('profil_detail/(?P<pk>\d+)', views.ProfilDetailView.as_view(), name='profil_detail'),
    path('edit_profil/(?P<pk>\d+)', views.ProfilUpdateView.as_view(), name='edit_profil'),
]
