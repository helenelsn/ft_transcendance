import django_filters
from .models import Game, models

class GamesFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['name']

        
    @property
    def qs(self):   
        parent = super().qs
        pub = parent.filter(is_public=True)
        if self.request.user.is_authenticated:
            in_player = parent.filter(players__in=[self.request.user.profile])
            is_user =  parent.filter(user=self.request.user)
            visible_games = in_player.union(is_user.union(pub),)
        else:
            visible_games = pub
            
        return  visible_games