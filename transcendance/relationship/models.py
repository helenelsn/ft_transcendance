from django.db import models
from accounts.models import Profile 
# Create your models here.
class Relation(models.Model):
    myself = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL, related_name="myself")
    other = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL, related_name="other")
    relations = ((0, 'neutral'),
                (1, 'friend'),
                (2, 'friend_request'),
                (3,'blocked'),
                (4, 'blocked_by'),
                )
    relation = models.IntegerField(choices=relations, default=0)
    
    
    def __str__(self):
        return self.user.username