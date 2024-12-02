from django.db import models
from accounts.models import User
# Create your models here.


# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(default='Wonderfull tournament')
    end = models.BooleanField(default=False)
    
    public = models.BooleanField(default=False)
    number_players = models.IntegerField(default=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    begin = models.DateTimeField(auto_now_add=True)
    players =models.ManyToManyField(User)
    
    
    def __str__(self) -> str:
        return f"{self.name}"
    # class Meta: