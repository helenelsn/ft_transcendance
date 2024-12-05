import django_tables2 as tables
from .models import User
from relationship.models import Relation 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn
from .abstract_view import RelationView
from django.db.models import Count, F, Value

def relation_class(**kwargs):
    if kwargs['table'] is None or kwargs['record'] is None:
        return
    from_user = kwargs['table'].request.user
    to_user = kwargs['record']
    return Relation.str_relation_between(from_user, to_user)
   

class AllUserTable(tables.Table):
    username =  tables.Column(verbose_name='Users')
    id = tables.Column(verbose_name='Actions')
    class Meta:
        model = User
        row_attrs = {
            "scope": relation_class
        }
        fields = ( 'username', 'id')
        
        
    def render_id(self, value, record):
        if self.request.user.is_authenticated:
            actions = RelationView.get_relation_actions(Relation.relation_between(from_user=self.request.user.id, to_user=value))
            
            return format_html(' | '.join([f"<a href={reverse(actions[name], args=[record.username])}> {name} </a>" for name in actions]))
        else:
            return '---'
        
    def render_username(self, value, record):
        return format_html(f"<a href={reverse('accounts:profil_detail', args=[value,])}> {value} </a>")
       
       
        