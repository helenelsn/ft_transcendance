from django.db import models
from accounts.models import User, Profile
from notifications.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver
from event.models import Event
from django.urls import reverse


class Game(Event):
    max_players = 2
    # history = models.OneToOneField(GameHistory, on_delete=models.CASCADE)
    
    @property
    def absolute_url(self):
        return "games:game_detail"
    
    def __str__(self):
        return f'game {super(Event, self)}' 

        
# class GameHistory(EventHistory):
#     pass
#     game = models.OneToOneField(Game, on_delete=models.CASCADE)
#     start_time = models.DateTimeField(null=True)
#     duration = models.DurationField(null=True)
#     over = models.BooleanField(default=False)
#     left_score = models.PositiveIntegerField(default=0)
#     right_score = models.PositiveIntegerField(default=0)
    
#     @receiver(post_save, sender=Game)
#     def create_or_update_game_history(sender, instance, created, **kwargs):
#         history, created = GameHistory.objects.get_or_create(game=instance)
#         history.save()
        
#     @property
#     def equality(self):
#         return self.left_score == self.right_score
    
#     def is_winner(self, user):
#         return (user==self.game.left_player and self.left_score > self.right_score) or (user==self.game.right_player and self.right_score > self.left_score)
        
#     def is_loser(self, user):
#         return not self.is_winner(user) and not self.equality
        
    
#     @property
#     def winner(self):
#         if not self.over:
#             return 
#         if self.equality:
#             return [self.game.left_player, self.game.right_player]
#         if self.left_score > self.right_score:
#             return self.game.left_player
#         return self.game.right_player
    
#     @property
#     def loser(self):
#         if not self.over or self.equality:
#             return 
#         if self.left_score < self.right_score:
#             return self.game.left_player
#         return self.game.right_player
        
#     @property
#     def winner_score(self):
#         return self.left_score if self.left_score > self.right_score else self.right_score
    
#     @property
#     def loser_score(self):
#         return self.left_score if self.left_score < self.right_score else self.right_score
        
#     def __str__(self):
#         return f'{self.game}'
        
        
    
    
        
class GameInvitation(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'You re invited to game {self.game.name}'
        
class GameLaunching(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'Game {self.game.name} is beginning!'


