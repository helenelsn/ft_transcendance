import django_tables2 as tables
from relationship.models import Relation 
from relationship.abstract_view import RelationView
from .models import User
from django.utils.html import format_html
from django.urls import reverse

def relation_class(**kwargs):
    if kwargs['table'] is None or kwargs['record'] is None:
        return
    from_user = kwargs['table'].request.user
    to_user = kwargs['record']
    return Relation.str_relation_between(from_user, to_user)
   

class UserTable(tables.Table):
    username =  tables.Column(verbose_name='Users')
    id = tables.Column(verbose_name='Actions')

    class Meta:
        model = User
        row_attrs = {
            "scope": relation_class
        }
        fields = ( 'username', 'id')
        
    def render_username(self, value, record):
        return format_html(f"<a href={reverse('accounts:profil_detail', args=[record.id,])}> {value} </a>")
    
    def render_id(self, value, record):
        if self.request.user.is_authenticated:
            if self.request.user.id == value:
                return format_html(f"<a href={reverse('accounts:edit_profil', args=[value])}> edit </a>")
            else:
                actions = RelationView.get_relation_actions(Relation.relation_between(from_user=self.request.user.id, to_user=value))
                return format_html(' | '.join([f"<a href={reverse(actions[name], args=[record.username])}> {name} </a>" for name in actions]))
        else:
            return '---'
        
       
        