from .models import Tournament 
import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from tournaments.abstract_views import TournamentView


class TournamentTable(tables.Table):
    
    class Meta:
        model = Tournament
        fields = ( 'name', 'number_players', 'players')

    def render_name(self, record):
        return TournamentView(record).linked_name