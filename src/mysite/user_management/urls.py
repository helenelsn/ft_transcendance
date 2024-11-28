from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.all_user),
    path("signin", views.sign_in),
]