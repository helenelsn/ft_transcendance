from django.db import models

from accounts.models import User
from abc import ABC, abstractmethod
from django.urls import reverse
from accounts.models import User
from notifications.models import Notification
    

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=30, default='event!')
    description = models.TextField(default='event description')
    is_public = models.BooleanField(default=False)
    players = models.ManyToManyField(User, related_name='players', through="EventPlayer")
    max_player = 1
    start_time = models.DateTimeField(null=True)
    over = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse(self.absolute_url, kwargs={"pk": self.pk})


    def get_index_url(self):
        return reverse(self.index_url,)

    @property
    def is_full(self) -> bool:
        return self.player_count == self.max_player
    
    @property
    def player_count(self) -> int :
        return len(self.players)
        
    @property
    def is_over(self) -> bool:
        return self.over

    def register_player(self, user_pk):
        user = User.objects.get(pk=user_pk)
        if not self.is_full:
            self.players.add(user)
            self.save()
        else:
            # todo=> send alreadry full message
            pass
        
    def remove_player(self, user_pk):
        to_del = self.players.filter(players__in=[user_pk])
        if to_del is None:
            #todo => raise exp
            return
        self.players.remove(to_del)
        
    def user_registerd(self, user_pk):
        return len(self.players.filter(players__in=[user_pk])) > 0

    def user_is_owner(self, user_pk):
        return self.owner.pk == user_pk
    
    def __str__(self):
        return f'{self.name} {self.id}'
    

class EventPlayer(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    
    
class EventInvitation(Notification):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    @staticmethod
    def create(user: User, event : Event):
        invite = EventInvitation.objects.create(user=user, event=event, message = f'You re invited to event')
        
    
    def __str__(self):
        return f'You re invited to event {self.event}'