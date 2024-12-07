import django_tables2 as tables
from accounts.models import Profile, User
from .models import Game 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils



class GamesTable(tables.Table):
    join = tables.Column(empty_values=[])
    
    class Meta:
        model = Game
        fields = ( 'name', )
        # row_attrs = {
        #     "scope": lambda record: Relation.relations[record.relation]
        # }
        
    def render_name(self, record : Game):
        return record.get_absolute_url()
    def render_join(self, record : Game):
        return format_html('join')
        
