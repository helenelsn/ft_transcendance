from django.db import models
from accounts.models import User

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def filter_user_notifs(user):
        return Notification.objects.filter(user=user)
    
    @staticmethod
    def filter_notif(notif_id, user):
        return Notification.filter_user_notifs( user,).filter(pk=notif_id)
    
    def __str__(self):
        return self.message
    