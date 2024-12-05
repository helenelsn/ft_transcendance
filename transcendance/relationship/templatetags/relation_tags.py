from django import template
register = template.Library()
from relationship.tables import RelationTable
from relationship.models import Relation, FRIEND, OTHER_REQUEST, REQUEST, BLOCKED

trs = {
        'friend' : 0,
        'request' :1 ,
        'other_request':2,
        'neutral':3,
        'blocked':4,
    }

def get_user_relations(request):
    return Relation.objects.filter(from_user=request.user)

@register.simple_tag
def user_relation_table(request, rel_type):
    print(rel_type)
    qs = get_user_relations(request).filter(relation=trs[rel_type])
    print(qs)
    if request.user.is_authenticated and len(qs) > 0:
        return RelationTable(qs, request=request, )

@register.simple_tag
def interesting_relationship():
    return {'friend':'Friends', 'request':'Pending request', 'other_request' : 'Sent you a friend request', }

@register.simple_tag
def get_trs():
    return trs