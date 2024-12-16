
from django_filters import FilterSet
from .models import Relation, FRIEND

class RelationFilter(FilterSet):
    class Meta:
        model = Relation
        fields = {"relation": ["exact"], "to_user__username": ["contains"]}
        
    @property
    def qs(self):
        parent = super().qs
        return parent.filter(from_user=self.request.user.id).order_by('relation')

class FriendFilter(RelationFilter):
    class Meta(RelationFilter.Meta):
        fields = {"to_user__username": ["contains"]}
        
    @property
    def qs(self):
        parent = super(FriendFilter, self).qs
        return parent.filter(relation=FRIEND)