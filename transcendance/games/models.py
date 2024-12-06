from django.db import models
from accounts.models import User

class Game(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin")
    players = models.ManyToManyField(User, blank=True)
    is_public = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse("games:games_detail", kwargs={"pk": self.pk})