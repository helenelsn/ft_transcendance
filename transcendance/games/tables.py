import django_tables2 as tables
from accounts.models import Profile, User
from .models import Game 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from games.templatetags import game_tags

def game_scope(**kwargs):
    if kwargs['table'] is None or kwargs['table'].request is None or not kwargs['table'].request.user.is_authenticated or kwargs['record'] is None:
        return
    r_user = kwargs['table'].request.user
    
    if kwargs['record'].user == r_user:
        return 'owned_game'
    if kwargs['record'].left_player == r_user  or kwargs['record'].right_player == r_user :
        return 'play_in_game'
    return 'neutral_game'

class GamesTable(tables.Table):
    # name = tables.Column(verbose_name='Name', empty_values=[])
    left_player__username = tables.Column(verbose_name='Player 0')
    right_player__username = tables.Column(verbose_name='Player 1')
    join = tables.Column(verbose_name='Join', empty_values=[])
    
    class Meta:
        model = Game
        fields = ('name', 'left_player__username', 'right_player__username')
        row_attrs = {
            # "scope": game_scope
        }
        
    def render_name(self, record : Game):
        return html_utils.format_hyperlink(link=record.get_absolute_url(), display=record.name)
    
    def render_left_player__username(self, value, record : Game):
        return html_utils.format_hyperlink(link=record.left_player.profile.get_absolute_url(), display=value)
    
    def render_right_player__username(self, value, record : Game):
        return html_utils.format_hyperlink(link=record.right_player.profile.get_absolute_url(), display=value)
        
    def render_join(self, record : Game):
        if self.request.user.is_authenticated:
            return game_tags.game_actions(self.request.user, record)
        return html_utils.format_html('accounts:login', 'login to join')
