import django_filters
from .models import Tournament, models
from django.forms import CheckboxInput

class TournamentFilter(django_filters.FilterSet):
    class Meta:
        model = Tournament
        fields = {'name': ['contains']}
        
    @property
    def qs(self):
        parent = super().qs
        return parent