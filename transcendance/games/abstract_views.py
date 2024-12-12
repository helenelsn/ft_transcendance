
from django.shortcuts import render, redirect
from django.urls import reverse
from common.utils import redir_to, redir_to_index
from .models import Game, GameInvitation, GameLaunching, GameHistory
from accounts.models import User
from django.contrib.auth.decorators import login_required
from common.templatetags import html_utils

class GameView():
    def __init__(self, game : Game):
        self.game = game
        
    def get_actions(self, user):
        actions = {}
        if self.game.is_over or not self.game.user_in_game(user):
            return actions
        if not self.game.is_full and self.game.is_public:
            actions.update({ reverse('games:join_game_players', args=[self.game.id, user.id]): 'join'})
        if self.game.is_full:
            actions.update({ reverse('games:launch_game', args=[self.game.id]): 'launch'})
        else:
            actions.update({ reverse('relationship:game_invite_players', args=[self.game.id]): 'invite player'})
        
        actions.update({
                        reverse('games:unjoin_game_players', args=[self.game.id, user.id]) : 'unjoin',
                        reverse('games:delete_game', args=[self.game.id]) : 'delete',
                       })
        return actions

    @staticmethod
    def game_actions(game, user):
        actions = GameView(game).get_actions(user)
        return html_utils.html_list_join([html_utils.format_hyperlink(key, val) for key, val in actions.items()], sep = ' | ')
    
    @login_required
    def create(request):
        game = Game(left_player=request.user)
        game.save()
        return redirect('games:settings', game.id)
    
    @login_required        
    def delete_game(request, pk):
        Game.objects.filter(pk=pk).delete()
        return redir_to_index('games')
    
    @login_required
    def join_players(request, pk, player_pk):
        game = Game.objects.get(pk=pk)
        game.add_player(player_pk)
        return redirect(game.get_absolute_url())
    
    @login_required
    def unjoin_game_players(request, pk, player_pk):
        game = Game.objects.get(pk=pk)
        game.remove_player(player_pk)
        return redir_to_index('games')
    
    @login_required
    def invite_player(request, pk, player_pk):
        game = Game.objects.get(pk=pk)
        user = User.objects.get(pk=player_pk)
        message = f'user {request.user.username} invited you to join game {game.name}'
        notif = GameInvitation(user=user, game=game, message=message)
        notif.save()
        return redirect(game.get_absolute_url())

    @login_required
    def launch_game(request, pk):
        game = Game.objects.get(pk=pk)
        message = f'Game {game.name} beginning'
        user = game.left_player
        notif = GameLaunching(user=user, game=game, message=message)
        notif.save()
        user = game.right_player
        notif = GameLaunching(user=user, game=game, message=message)
        notif.save()
        
        history = GameHistory.objects.get(game=game)
        return redirect(reverse("games:game", args=[history.pk]))
