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
    relation = tables.Column(verbose_name='Actions')
    
    class Meta:
        model = Relation
        row_attrs = {
            "scope": lambda record: Relation.relations[record.relation]
        }
        fields = ( 'to_user', 'relation')
        
    def order_to_user(self, queryset, is_descending : bool):
        on= '-relation' if is_descending else 'relation'
        return (queryset.order_by(on), True)
        
    def render_relation(self, record : Relation):
        if self.request and self.request.user.is_authenticated:
            if self.request.user == record.to_user:
                return html_utils.a_hyperlink('accounts:edit_profil', display='edit', args=record.relation)
            return RelationView.get_formated_relation_actions(self.request, record.to_user)
        else:
            return '---'
        
    def render_to_user(self, value : str, record : Relation):
        return format_html(f"<a href={record.to_user.profile.get_absolute_url()}> {value} </a>")
