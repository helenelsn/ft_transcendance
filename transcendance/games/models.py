from django.db import models
from accounts.models import User, Profile
from notifications.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver

class Game(models.Model):
    name = models.CharField(max_length=30, default='Game!')
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    left_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='left_player', null=True)
    right_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='right_player', null=True)
    is_public = models.BooleanField(default=False)
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
        # else:
        #     raise Exception('Trying to add player to a full game')
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
        return self.user_is_player(user)
    
    def user_is_player(self, user):
        return user==self.left_player or user==self.right_player
        
        
    def get_other_player(self, user):
        if self.left_player==user:
            return self.right_player
        return self.left_player

    @property
    def is_full(self) -> bool:
        return self.player_count == 2
    
    @property
    def player_count(self) -> int :
        count = 0
        if self.left_player is not None:
            count += 1
        if self.right_player is not None:
            count += 1
        return count
        
    @property
    def is_over(self) -> bool:
        return self.gamehistory.over

    def __str__(self):
        return f'{self.name} {self.id}'

        
class GameHistory(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)
    over = models.BooleanField(default=False)
    left_score = models.PositiveIntegerField(default=0)
    right_score = models.PositiveIntegerField(default=0)
    
    @receiver(post_save, sender=Game)
    def create_or_update_game_history(sender, instance, created, **kwargs):
        history, created = GameHistory.objects.get_or_create(game=instance)
        history.save()
        
    @property
    def equality(self):
        return self.left_score == self.right_score
    
    def is_winner(self, user):
        return (user==self.game.left_player and self.left_score > self.right_score) or (user==self.game.right_player and self.right_score > self.left_score)
        
    def is_loser(self, user):
        return not self.is_winner(user) and not self.equality
        
    
    @property
    def winner(self):
        if not self.over:
            return 
        if self.equality:
            return [self.game.left_player, self.game.right_player]
        if self.left_score > self.right_score:
            return self.game.left_player
        return self.game.right_player
    
    @property
    def loser(self):
        if not self.over or self.equality:
            return 
        if self.left_score < self.right_score:
            return self.game.left_player
        return self.game.right_player
        
    @property
    def winner_score(self):
        return self.left_score if self.left_score > self.right_score else self.right_score
    
    @property
    def loser_score(self):
        return self.left_score if self.left_score < self.right_score else self.right_score
        
    def __str__(self):
        return f'{self.game}'
        
        
    
    
        
class GameInvitation(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'You re invited to game {self.game.name}'
        
class GameLaunching(Notification):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'Game {self.game.name} is beginning!'


