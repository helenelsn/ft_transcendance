from django.db import models
from accounts.models import User, Profile
from notifications.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver
from event.models import Event
from django.urls import reverse


class Game(Event):
    max_players = 2
    absolute_url = "games:detail"
    
        
# class GameInvitation(Notification):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
#     def __str__(self):
#         return f'You re invited to game {self.game.name}'
        
class GameLaunching(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'Game {self.game.name} is beginning!'


