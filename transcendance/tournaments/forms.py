from typing import Any
from django import forms
from .models import TournamentPlayer, Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'bio']
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("3 letter min")
        return name
    
    # def clean(self) -> dict[str, Any]:
    #     #form global rules
    #     return super().clean()