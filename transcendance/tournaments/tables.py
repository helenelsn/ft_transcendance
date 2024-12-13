from .models import Tournament 
import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils


class TournamentTable(tables.Table):
    react = tables.Column(empty_values=[])
    
    class Meta:
        model = Tournament
        fields = ( 'name', 'number_players', 'players')