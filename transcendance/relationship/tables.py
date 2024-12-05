import django_tables2 as tables
from accounts.models import Profile, User
from .models import Relation 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn
from django.db.models import Count, F, Value
from .abstract_view import RelationView
class RelationTable(tables.Table):
    to_user = tables.Column(verbose_name='User')
    relation = tables.Column(verbose_name='Actions')
    
    class Meta:
        model = Relation
        row_attrs = {
            "scope": lambda record: Relation.relations[record.relation]
        }
        fields = ( 'to_user', 'relation')
        
    def order_to_user(self, queryset, is_descending):
        on= '-relation' if is_descending else 'relation'
        return (queryset.order_by(on), True)
        
    def render_relation(self, value, record):
        if self.request.user.is_authenticated:
            if self.request.user == record.to_user:
                return format_html(f"<a href={reverse('accounts:edit_profil', args=[value])}> edit </a>")
            return RelationView.get_formated_relation_actions(self.request, record.to_user)
        else:
            return '---'
        
    def render_to_user(self, value, record):
        return format_html(f"<a href={reverse('accounts:profil_detail', args=[record.to_user.id,])}> {value} </a>")
