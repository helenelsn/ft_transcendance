from django import template

from common.templatetags import html_utils
from accounts.templatetags import accounts_tags

from games.models import Game
# from relationship.tables import RelationTable, Relation
from games.abstract_views import GameView
register = template.Library()
app_name='games'


@register.simple_tag
def show_players(game : Game):
    if game.player_count == 2:
        return html_utils.format_p(f'{accounts_tags.profil_detail_link(game.left_player)} vs {accounts_tags.profil_detail_link(game.right_player)}')
    elif game.player_count == 1:
        player = game.left_player if game.left_player is not None else game.right_player
        return html_utils.format_p(f'{accounts_tags.profil_detail_link(player)} is waiting for an brave opponent ...')
    else:
        return html_utils.format_p(f'No players yet')
            
@register.simple_tag
def game_actions(user, game:Game):
    
    return GameView(object=game).get_actions(user=user)
        
@register.simple_tag
def game_result(game : Game):
    if not game.is_over:
        return html_utils.format_html('')
    return GameView(game=game).game_over_view()
   
@register.simple_tag
def  user_games_resume(user):
    return GameView.user_resume(user)
    

    