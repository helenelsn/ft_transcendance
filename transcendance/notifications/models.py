from django.db import models
from accounts.models import User
from abc import ABC, abstractmethod

# add type 
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # def get_actions(self):
    @staticmethod
    def filter_user_notifs(user):
        return Notification.objects.filter(user=user).order_by('timestamp')
    
    @staticmethod
    def filter_notif(notif_id, user):
        return Notification.filter_user_notifs( user,).filter(pk=notif_id)
    
    @staticmethod
    def get_user_notifs(user):
        return Notification.filter_user_notifs(user).all()
    
    @staticmethod
    def get_user_unreads_notifs(user):
        return Notification.filter_user_notifs(user).filter(is_read=False).all()
    
    @staticmethod
    def delete(notif):
        Notification.objects.filter(pk=notif).delete()
    
    def __str__(self):
        return self.message
    
