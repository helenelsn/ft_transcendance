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
    

class OpenGamesFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = {'name': ['contains'], 'left_player__username': ['contains'], 'right_player__username': ['contains']}

    @property
    def qs(self):   
        parent = super().qs
        parent = parent.filter(gamehistory__over=False).filter(is_public=True).exclude(left_player=self.request.user).exclude(right_player=self.request.user)
        
        left_void = parent.filter(left_player=None)
        right_void = parent.filter(right_player=None)
        return  left_void.union(right_void)
    
    
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