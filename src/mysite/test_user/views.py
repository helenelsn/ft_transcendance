from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse("On vise toujour la lune parfois ca tombe sur un pouuuletfrom coucou le hibou")

def all_user(request):
    return HttpResponse("all user")

def sign_in(request):
    return render(request, "test_user/chouchou.html", {})

from .models import User
def user_page(request, user):
    try:
        u = User.objects.get(name=user)
    except User.DoesNotExist:
        raise Http404("hfdsjbfhjksdbfkwe")
    
    return render(request, "test_user/account.html", {"user": u})


# from django.shortcuts import render

# from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/account.html", context)