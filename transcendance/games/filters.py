import django_filters
from .models import Game, models

class GamesFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['name']

        
    @property
    def qs(self):   
        parent = super().qs
        visible_games = parent.filter(is_public=True)
        if self.request.user.is_authenticated:
            is_owner = parent.filter(owner=self.request.user)
            is_left = parent.filter(left_player=self.request.user)
            is_right = parent.filter(right_player=self.request.user)
            visible_games = is_right.union(is_left.union(is_owner.union(visible_games)))
            
        return  visible_games