from django import template

from common.templatetags import html_utils
from accounts.templatetags import accounts_tags

from games.models import Game, GameHistory
from relationship.tables import RelationTable, Relation
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
    if not game.is_full and not game.user_is_player(user) and not game.is_over:
        return html_utils.a_hyperlink('games:join_game_players', args=[game.id, user.id], display='join')
    if not game.user_in_game(user):
        return
    lst = []
    if not game.is_over:
        if not game.is_full:
            lst.append(html_utils.a_hyperlink('relationship:game_invite_players', args=game.id, display='invite player'))
            
        if game.user_is_player(user):
            if game.is_full:    
                lst.append(html_utils.a_hyperlink('games:launch_game', args=game.id, display='launch'))
            lst.append(html_utils.a_hyperlink('games:unjoin_game_players', args=[game.id, user.id], display='unjoin'))
            
        if game.owner==user:
            lst.append(html_utils.a_hyperlink('games:delete_game', args=game.id, display='delete'))
    return html_utils.html_list_join(lst, sep=' | ')
        
    