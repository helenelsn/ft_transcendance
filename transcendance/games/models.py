from django.db import models
from accounts.models import User, Profile
from notifications.models import Notification

class Game(models.Model):
    name = models.CharField(max_length=30, default='Game!')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    left_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='left_player', null=True)
    right_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='right_player', null=True)
    is_public = models.BooleanField(default=False)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', null=True)
    max_players = 2

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("games:game_detail", kwargs={"pk": self.pk})

    def add_player(self, user_pk):
        user = User.objects.get(pk=user_pk)
        if self.left_player == user or self.right_player == user:
            return
            # raise Exception('trying to add a player who s already in game')
        if self.left_player is None:
            self.left_player = user
        elif self.right_player is None:
            self.right_player = user
        else:
            raise Exception('Trying to add player to a full game')
        self.save()

    def remove_player(self, user_pk):
        user = User.objects.get(pk=user_pk)
        if self.left_player == user:
            self.left_player = None
        elif self.right_player == user:
            self.right_player = None
        else:
            raise Exception('Trying to remove a player that was not part of that game!')
        self.save()
        
    def user_in_game(self, user):
        return user==self.owner or self.user_is_player(user)
    
    def user_is_player(self, user):
        return user==self.left_player or user==self.right_player

    @property
    def is_full(self):
        return self.player_count == 2
    
    @property
    def player_count(self):
        count = 0
        if self.left_player is not None:
            count += 1
        if self.right_player is not None:
            count += 1
        return count
        

    def __str__(self):
        return self.name

        
        
class GameInvitation(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'You re invited to game {self.game.name}'
