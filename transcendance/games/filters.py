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
        # parent = parent.exclude(id__in=pub)
        in_player = parent.filter(players__in=[self.request.user.profile])
        # parent = parent.exclude(id__in=in_player)
        is_user =  parent.filter(user=self.request.user)
        visible_games = in_player.union(is_user.union(pub),)
        # print(f'pub: {pub}\nin_player: {in_player}\nis_user: {is_user}\n\ntot: {pub + in_player + is_user}')
        return  visible_games