from django.db import models

# Create your models here.
class TournamentPlayer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(default='Wonderfull tournament')
    end = models.BooleanField(default=False)
    
    number_players = models.IntegerField(default=4)
    players = models.ManyToManyField(TournamentPlayer)
    
    def __str__(self) -> str:
        return f"{self.name}"
    # class Meta: