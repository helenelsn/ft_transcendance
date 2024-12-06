from django import template
from common.templatetags import html_utils
from games.models import Game
from relationship.tables import RelationTable, Relation

register = template.Library()
app_name='games'

from notifications.templatetags import notif_tags
@register.inclusion_tag(filename='utils/table.html', takes_context=True)
def show_players(context, request, game : Game):
    players = [p.user for p in game.players.all()]
    qs = Relation.objects.filter(to_user__in=players).filter(from_user=request.user)
    context['table'] = RelationTable(qs, request=request)
    return context

@register.simple_tag
def tag_invite_player(object):
    return html_utils.a_hyperlink('relationship:game_invite_players', display='invite players', args=object.id)
    