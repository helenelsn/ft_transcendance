import django_tables2 as tables
from .models import Relation 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn
from django.db.models import Count, F, Value
from .abstract_view import RelationView
from common.templatetags import html_utils


class RelationTable(tables.Table):
    to_user = tables.Column(verbose_name='User')
    actions = tables.Column(verbose_name='Actions', empty_values=[])
    
    class Meta:
        model = Relation
        row_attrs = {
            "scope": lambda record: Relation.relations[record.relation]
        }
        fields = ( 'to_user',)
        
    def order_to_user(self, queryset, is_descending : bool):
        on= '-relation' if is_descending else 'relation'
        return (queryset.order_by(on), True)

    def render_actions(self, record : Relation):
        if self.request and self.request.user.is_authenticated:
            if self.request.user == record.to_user:
                return html_utils.a_hyperlink('accounts:edit_profil', display='edit', args=record.to_user.pk)
            return RelationView.get_formated_relation_actions(self.request, record.to_user)
        else:
            return '---'
       
        
    def render_to_user(self, value : str, record : Relation):
        return format_html(f"<a href={record.to_user.profile.get_absolute_url()}> {value} </a>")

class FriendGameInviteTable(RelationTable):
    invitation = tables.Column(empty_values=[])
    
    def __init__(self, data=None, order_by=None, orderable=None, empty_text=None, exclude=None, attrs=None, row_attrs=None, pinned_row_attrs=None, sequence=None, prefix=None, order_by_field=None, page_field=None, per_page_field=None, template_name=None, default=None, request=None, show_header=None, show_footer=True, extra_columns=None, game=None):
        self.game = game
        super().__init__(data, order_by, orderable, empty_text, exclude, attrs, row_attrs, pinned_row_attrs, sequence, prefix, order_by_field, page_field, per_page_field, template_name, default, request, show_header, show_footer, extra_columns)
    
    def render_invitation(self, record : Relation):
        return html_utils.a_hyperlink('games:invite_player', display='invite to join game', args=[self.game, record.to_user.id])