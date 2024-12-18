from django.db import models
from accounts.models import User
from abc import ABC, abstractmethod

# add type 
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    @property
    def name(self):
        return self.message if len(self.message) < 20 else self.message[:17] + '...'
    
    @staticmethod
    def filter_user_notifs(user : User):
        return Notification.objects.filter(user=user).order_by('timestamp')
    
    @staticmethod
    def get_user_unreads_notifs(user : User):
        return Notification.filter_user_notifs(user).filter(is_read=False)
    
    @staticmethod
    def delete(notif):
        Notification.objects.filter(pk=notif).delete()
    
    def __str__(self):
        return self.message
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("notifications:detail", kwargs={"pk": self.pk})

class Invitation(Notification):
    @property
    def valid():
        return True
    pass