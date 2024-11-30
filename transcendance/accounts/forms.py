from typing import Any
from django import forms
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm

class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        
class ProfileChangeForms():
    def __init__(self, request, type="") -> None:
        if request.method == 'POST':
            self.profile_form = ProfileChangeForm(request.POST, instance = Profile.objects.filter(user=request.user).get())
            self.user_form = UserChangeForm(request.POST, instance = request.user)
            if self.is_valid():
                self.save()
                # return redirect(f"{app_name}:index")
        else:
            self.profile_form = ProfileChangeForm(instance = Profile.objects.filter(user=request.user).get())
            self.user_form = UserChangeForm(instance = request.user)
    
    def is_valid(self):
        return self.profile_form.is_valid()
        return all([f.is_valid() for f in self.to_set()])
    
    def save(self):
        print("--------------saved-------------------")
        self.profile_form.save()
        self.user_form.save() 
    
    def to_set(self) -> set :
        return [self.user_form, self.profile_form]
    
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 3:
    #         raise forms.ValidationError("3 letter min")
    #     return name
    

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['friends']