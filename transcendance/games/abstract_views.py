
from django.shortcuts import render, redirect
from django.urls import reverse
from common.utils import redir_to, redir_to_index
from .models import Game, GameInvitation, GameLaunching, GameHistory
from accounts.models import User
from django.contrib.auth.decorators import login_required
from common.templatetags import html_utils

class GameView():
    def __init__(self, game):
        if isinstance(game, Game):
            self.game : Game = game
            self.history : GameHistory = game.gamehistory
        else:
            self.history : GameHistory = game
            self.game : Game = self.history.game
        
    def get_actions(self, user):
        actions = {}
        if self.game.is_over or not self.game.user_in_game(user):
            if not self.game.is_full and self.game.is_public:
                actions.update({ reverse('games:join_game_players', args=[self.game.id, user.id]): 'join'})
            return actions
        if self.game.is_full:
            actions.update({ reverse('games:launch_game', args=[self.game.id]): 'launch'})
        else:
            actions.update({ reverse('relationship:game_invite_players', args=[self.game.id]): 'invite player'})
        actions.update({
                        reverse('games:unjoin_game_players', args=[self.game.id, user.id]) : 'unjoin',
                        reverse('games:delete_game', args=[self.game.id]) : 'delete',
                       })
        return actions
    
    @property
    def winner_links(self):
        if not self.game.is_over:
            return
        winner = self.game.gamehistory.winner
        if isinstance(winner, list):
            return html_utils.html_list_join([html_utils.format_hyperlink(link=w.profile.get_absolute_url(), display=w.username) for w in winner], sep = ' | ') 
        return html_utils.format_hyperlink(link=winner.profile.get_absolute_url(), display=winner.username)
    
    @property
    def loser_links(self):
        if not self.game.is_over:
            return
        loser = self.game.gamehistory.loser
        if loser is not None:   
            return html_utils.format_hyperlink(link=loser.profile.get_absolute_url(), display=loser.username)
        
    def game_actions(self, user):
        actions = GameView(self.game).get_actions(user)
        return html_utils.html_list_join([html_utils.format_hyperlink(key, val) for key, val in actions.items()], sep = ' | ')
    
    def game_over_view(self):
        if not self.game.is_over:
            return
        if self.history.equality:
            return html_utils.format_html(f'<p> equality between {self.winner_links} with {self.history.left_score} points each</p>')
        return html_utils.html_list_join([f'{self.winner_links} win this game with {self.history.winner_score}',
                                          f'{self.loser_links} lose with  {self.history.loser_score}',], as_p=True)
    
    @staticmethod
    def user_resume(user):
        games = Game.objects.filter(left_player=user).filter(gamehistory__over = True)
        is_left = games.filter(left_player=user)
        is_right = games.filter(right_player=user)
        games = is_right.union(is_left)
        games = games.all()
        equality = 0
        wins = 0
        lose = 0
        for game in games:
            hist : GameHistory = game.gamehistory
            if hist.equality:
                equality += 1
            elif hist.is_winner(user):
                wins += 1
            elif hist.is_loser(user):
                lose += 1
        return html_utils.html_list_join([f'Wins : {wins}', f'equality : {equality}', f'lose : {lose}'], as_p=True)
        
        
    
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
