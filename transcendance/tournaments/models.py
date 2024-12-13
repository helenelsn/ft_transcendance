from django.db import models
from accounts.models import User
from django.urls import reverse
# Create your models here.


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100, default='Great tournament')
    bio = models.TextField(default='Wonderfull tournament')
    over = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    
    number_players = models.PositiveIntegerField(default=4)
    players = models.ManyToManyField(User)
    
    @staticmethod
    def create_tournament(user):
        t = Tournament.objects.create()
        t.players.add(user)
        t.save()
        return t

    def get_absolute_url(self):
        return reverse('tournaments:tournament_detail', args=[self.pk])
    
    def __str__(self) -> str:
        return f"{self.name}"
    # class Meta: