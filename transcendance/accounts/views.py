from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import Profile
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from .models import User


@login_required
def index(request):
    return redirect(request.user.profile.get_absolute_url())

class UserCreateView(FormView):
    template_name = 'utils/form.html'
    form_class = UserCreationForm
    success_url = '/accounts/login'
    
    def form_valid(self, form: UserCreationForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'utils/form.html'
    form_class = AuthenticationForm
    success_url =  '/accounts'
    
    def form_valid(self, form : AuthenticationForm) -> HttpResponse:
        login(self.request, form.get_user())
        return super().form_valid(form)
    
class ProfilUpdateView(UpdateView):
    model = Profile
    fields = ['avatar', 'bio']
    template_name = 'utils/form.html'
    success_url =  '/accounts'
    
class LogoutView(RedirectView):
    pattern_name = 'accounts:index'
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)

class ProfilDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profil_detail.html'
