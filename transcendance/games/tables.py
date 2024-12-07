import django_tables2 as tables
from accounts.models import Profile, User
from .models import Game 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils

def game_scope(**kwargs):
    # print('checking')
    if kwargs['table'] is None or kwargs['table'].request is None or not kwargs['table'].request.user.is_authenticated or kwargs['record'] is None:
        return
    r_user = kwargs['table'].request.user
    if Game.objects.filter(user=r_user):
        return 'owned_game'
    if Game.objects.filter(players__in=[r_user.profile]):
        return 'play_in_game'
    else:
        return 'neutral_game'

class GamesTable(tables.Table):
    join = tables.Column(empty_values=[])
    
    class Meta:
        model = Game
        fields = ( 'name', )
        row_attrs = {
            "scope": game_scope
        }
        
    def render_name(self, record : Game):
        return html_utils.format_hyperlink(link=record.get_absolute_url(), display=record.name)
        return None
        # return html_utils.a_hyperlink(redir=record.get_absolute_url(), display=record.name)
    def render_join(self, record : Game):
        return record.get_absolute_url()
        # return None
        
