from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default="lorem")
    friends = models.ManyToManyField('self', symmetrical=True,)
    # friend_requests = models.ManyToManyField('self', symmetrical=False, )
    

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        profile, created = Profile.objects.get_or_create(user=instance)  
        profile.save()

    def __str__(self):
        return self.user.username

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # type => defining actions 
    # base_action : delete, mark as read/unread
    # invitation : accept /decline => read
    
    def __str__(self):
        return self.message
    