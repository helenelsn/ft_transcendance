import django_tables2 as tables
from accounts.models import Profile, User
from .models import Game, GameHistory 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from games.templatetags import game_tags
from .abstract_views import GameView
from accounts.views import ProfileView
def game_scope(**kwargs):
    if kwargs['table'] is None or kwargs['table'].request is None or not kwargs['table'].request.user.is_authenticated or kwargs['record'] is None:
        return
    r_user = kwargs['table'].request.user
    game = kwargs['record']
    if isinstance(game, GameHistory):
        game = game.game
    if not game.user_is_player(r_user):
        return 'neutral_game'
    if not game.is_over:
        if not game.is_full:
            return 'waiting_game_player'
        return 'waiting_game'
    history = game.gamehistory
    if history.equality:
        return 'equal_game'
    if history.is_winner(r_user):
        return 'winned_game'
    return 'losed_game'

class GamesTable(tables.Table):
    left_player__username = tables.Column(verbose_name='Player 0')
    right_player__username = tables.Column(verbose_name='Player 1')
    action = tables.Column(verbose_name='action', empty_values=[])
    
    class Meta:
        model = Game
        fields = ('name', 'left_player__username', 'right_player__username')
        row_attrs = {
            "scope": game_scope
        }
        
    def render_name(self, record : Game):
        return GameView(record).linked_name
        return html_utils.format_hyperlink(link=record.get_absolute_url(), display=record.name)
    
    def render_left_player__username(self, value, record : Game):
        return ProfileView(record.left_player.profile).linked_name
    
    def render_right_player__username(self, value, record : Game):
        return ProfileView(record.right_player.profile).linked_name
        
    def render_action(self, record : Game):
        return GameView(game=record).game_actions(user=self.request.user)


class GamesHistoryTable(tables.Table):
    winner = tables.Column(empty_values=[])
    loser = tables.Column(empty_values=[])
    
    class Meta:
        model = GameHistory
        fields = ('game__name', )
        row_attrs = {
            "scope": game_scope
        }
    
    def render_game__name(self, record : GameHistory):
        return html_utils.format_hyperlink(link=record.game.get_absolute_url(), display=record.game.name)
        
    def render_winner(self, record : GameHistory):
        return GameView(record.game).winner_links
    
    def render_loser(self, record: GameHistory):
        link = GameView(record.game).loser_links
        return link if link is not None else 'x'
        