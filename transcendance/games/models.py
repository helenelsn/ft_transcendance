from django.db import models
from accounts.models import User, Profile

class Game(models.Model):
    name = models.CharField(max_length=30, default='Game!')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(Profile, blank=True)
    is_public = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("games:game_detail", kwargs={"pk": self.pk})

    def add_player(self, user):
        self.players.add(Profile.objects.filter(user=user).get())
        self.save()

    def __str__(self):
        return self.name