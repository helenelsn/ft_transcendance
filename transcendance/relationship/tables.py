import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn
from django.db.models import Count, F, Value

from .models import Relation 
from .model_view import RelationView
from common.views import ActionModelView
from common.templatetags import html_utils
from common.global_view_mananger import get_view
from accounts.model_view import ProfileView
from common.tables import ActionsColumn, LinkedDetailNameColumn

class RelationTable(tables.Table):
    to_user = LinkedDetailNameColumn()
    actions = ActionsColumn()
    class Meta:
        model = Relation
        row_attrs = {
            "scope": lambda record: Relation.relations[record.relation]
        }
        fields = ( 'to_user',)
        
    
    
class FriendGameInviteTable(RelationTable):
    invitation = tables.Column(empty_values=[])
    
    def __init__(self, data=None, order_by=None, orderable=None, empty_text=None, exclude=None, attrs=None, row_attrs=None, pinned_row_attrs=None, sequence=None, prefix=None, order_by_field=None, page_field=None, per_page_field=None, template_name=None, default=None, request=None, show_header=None, show_footer=True, extra_columns=None, game=None):
        self.game = game
        super().__init__(data, order_by, orderable, empty_text, exclude, attrs, row_attrs, pinned_row_attrs, sequence, prefix, order_by_field, page_field, per_page_field, template_name, default, request, show_header, show_footer, extra_columns)
    
    def render_invitation(self, record : Relation):
        return html_utils.a_hyperlink('games:invite_player', display='invite to join game', args=[self.game, record.to_user.id])
    