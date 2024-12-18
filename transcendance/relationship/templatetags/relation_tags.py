from django import template
register = template.Library()

from relationship.models import Relation, FRIEND, OTHER_REQUEST, REQUEST, BLOCKED, NEUTRAL
from relationship.tables import RelationTable

trs = {
        'friend' : FRIEND,
        'request' : REQUEST,
        'other_request': OTHER_REQUEST,
        'neutral': NEUTRAL,
        'blocked':BLOCKED,
    }

@register.inclusion_tag('utils/tables.html', takes_context=True, )
def include_user_relations_tables(context, request):
    tables = {}
    for rel_type in trs.keys():
        if trs[rel_type] == NEUTRAL:
            continue
        qs = Relation.get_user_relations_qs(request.user).filter(relation=trs[rel_type])
        if qs.count() > 0 :
            tables[RelationTable(data=qs, request=request)] = rel_type
    context['tables'] = tables
    return context

@register.inclusion_tag('utils/table.html', takes_context=True, )
def include_user_friend_table(context, request):
    qs = Relation.get_user_relations_qs(request.user, rel_type=FRIEND)
    if qs.count() > 0 :
        table = RelationTable(qs, request=request)
        context['table'] = table
        context['table_title'] = f'friends:'
    return context

