import django_tables2 as tables
from relationship.models import Relation 
from relationship.abstract_view import RelationView
from .models import User
from django.utils.html import format_html
from django.urls import reverse
from common.templatetags import tags_utils

# def relation_class(**kwargs):
#     if kwargs['table'] is None or kwargs['record'] is None:
#         return
#     from_user = kwargs['table'].request.user
#     to_user = kwargs['record']
#     return Relation.str_relation_between(from_user, to_user)
   

# class UserTable(tables.Table):
#     username =  tables.Column(verbose_name='Users')
#     # id = tables.Column(verbose_name='Actions')

#     class Meta:
#         model = User
#         row_attrs = {
#             "scope": relation_class
#         }
#         fields = ( 'username', )
        
#     def render_username(self, value, record):
#         return format_html(f"<a href={reverse('accounts:profil_detail', args=[record.id,])}> {value} </a>")

        
       
        