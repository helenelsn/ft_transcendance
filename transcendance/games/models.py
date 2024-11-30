from django.db import models
from accounts.models import Profile

class Game(models.Model):
    players = models.ManyToManyField(Profile, limit_choices_to = 2)
    # invited = models.ManyToManyField(Profile, limit_choices_to = 2)
    # winner = models.ForeignKey(Profile, on_delete=)