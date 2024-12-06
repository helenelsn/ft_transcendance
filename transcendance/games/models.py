from django.db import models
from accounts.models import User, Profile

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(Profile, blank=True)
    is_public = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("games:game_detail", kwargs={"pk": self.pk})