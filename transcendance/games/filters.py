import django_filters
from .models import Game, models, GameHistory

class FurtherGamesFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['name', 'left_player', 'right_player']

        
    @property
    def qs(self):   
        parent = super().qs
        parent = parent.filter(gamehistory__over=False)
        if self.request.user.is_authenticated:
            is_left = parent.filter(left_player=self.request.user)
            is_right = parent.filter(right_player=self.request.user)
            visible_games = is_right.union(is_left)
            
        return  visible_games
    
    
class GameHistoryFilter(django_filters.FilterSet):
    class Meta:
        model = GameHistory
        fields = ['game__name', ]
    @property
    def qs(self):   
        parent = super().qs
        parent = parent.filter(over=True)
        
        if self.request.user.is_authenticated:
            is_left = parent.filter(game__left_player=self.request.user)
            is_right = parent.filter(game__right_player=self.request.user)
            visible_games = is_right.union(is_left)
            
        return  visible_games