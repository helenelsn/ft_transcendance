from django import template
register = template.Library()
from relationship.tables import RelationTable
from relationship.models import Relation, FRIEND, OTHER_REQUEST, REQUEST, BLOCKED, NEUTRAL
from relationship.abstract_view import RelationView

from django.utils.html import format_html
from django.urls import reverse
from common.templatetags.html_utils import index_hyperlink, a_hyperlink

app_name='relationship'
trs = {
        'friend' : FRIEND,
        'request' : REQUEST,
        'other_request': OTHER_REQUEST,
        'neutral': NEUTRAL,
        'blocked':BLOCKED,
    }

def get_user_relations(request):
    return Relation.objects.filter(from_user=request.user)

@register.inclusion_tag('utils/tables.html', takes_context=True, )
def include_user_relations_tables(context, request):
    if not request.user.is_authenticated:
        return
    tables = {}
    for rel_type in trs.keys():
        if trs[rel_type] == NEUTRAL:
            continue
        qs = get_user_relations(request).filter(relation=trs[rel_type])
        if len(qs) > 0 :
            tables[RelationTable(qs, request=request)] = rel_type
            
    context['tables'] = tables
    return context

@register.inclusion_tag('utils/table.html', takes_context=True, )
def include_other_user_friend_table(context, request, user):
    qs = Relation.objects.filter(from_user=user).filter(relation=FRIEND)
    print(qs)
    if len(qs) > 0 :
        table = RelationTable(qs, request=request)
        context['table'] = table
        # context['table_title'] = f'{user.username} friends:'
    return context

        
@register.simple_tag
def relation_index_hyperlink():
    return index_hyperlink(app_name)
    
@register.simple_tag
def relation_detail_hyperlink():
    return a_hyperlink(f'{app_name}:detail', 'all users')



@register.simple_tag
def relation_actions(request, other):
    return RelationView.get_formated_relation_actions(request, other)