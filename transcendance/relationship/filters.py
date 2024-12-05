
from django_filters import FilterSet
from .models import Relation

class RelationFilter(FilterSet):
    class Meta:
        model = Relation
        fields = {"relation": ["exact"], "to_user__username": ["contains"]}
        
    @property
    def qs(self):
        parent = super().qs
        return parent.filter(from_user=self.request.user.id).order_by('relation')