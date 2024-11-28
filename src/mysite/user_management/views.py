from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


# Create your views here.
def index(request):
    #si user connecte ->homepage
    #else =>
        # 2 bouton +jolidesign
        # log in
        # register
    return HttpResponse("On vise toujour la lune parfois ca tombe sur un pouuuletfrom coucou le hibou")

def all_user(request):
    return HttpResponse("all user")

def sign_in(request):
    return render(request, "user_management/sign_in.html", {})


def log_in(request):
    return render(request, "user_management/chouchou.html", {})




from .models import Profile
def user_page(request, user):
    try:
        u = Profile.objects.get(name=user)
    except Profile.DoesNotExist:
        raise Http404("hfdsjbfhjksdbfkwe")
    
    return render(request, "user_management/account.html", {"user": u})
