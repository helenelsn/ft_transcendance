import django_tables2 as tables
from accounts.models import Profile, User
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from games.templatetags import game_tags
from .views import EventView
from accounts.views import ProfileView
from .models import Event

# class ActionsColumn(tables.Column):

class EventsTable(tables.Table):
#     left_player__username = tables.Column(verbose_name='Player 0')
#     right_player__username = tables.Column(verbose_name='Player 1')
#     action = tables.Column(verbose_name='action', empty_values=[])
    
    class Meta:
        model = Event
        fields = ('name', 'players', 'actions')
        
    def render_name(self, record : Event):
        return EventView(record).detail_linked_name
        return html_utils.format_hyperlink(link=record.get_absolute_url(), display=record.name)
    
#     def render_left_player__username(self, value, record : Game):
#         return ProfileView(record.left_player.profile).linked_name
    
#     def render_right_player__username(self, value, record : Game):
#         return ProfileView(record.right_player.profile).linked_name
        
    # def render_action(self, record : Game):
    #     return GameView(game=record).game_actions(user=self.request.user)
