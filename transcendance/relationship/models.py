from django.db import models
from accounts.models import Profile 
# Create your models here.
class Relation(models.Model):
    # friend request
    # friends
    # bloqued
    # neutral
    myself = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="myself")
    other = models.ForeignKey(Profile, on_delete= models.CASCADE, related_name="other")
    relations = ((0, 'neutral'),
                (1, 'friend'),
                 (2, 'friend_request'),
                (3,'friend_request'),
                (4,'blocked'),
                (5, 'blocked_by'),
                )
    relation = models.CharField(choices=relations, max_length=20)
    # friends = models.ManyToManyField('self', symmetrical=True,)
    # friends_request = models.ManyToManyField('self', symmetrical=False,)
    
    # user = models.OneToOneField(, on_delete=models.CASCADE)
    # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    # bio = models.TextField(default="Add a bio!")
    # friend_requests = models.ManyToManyField('self', symmetrical=False, )
    
    def __str__(self):
        return self.user.username