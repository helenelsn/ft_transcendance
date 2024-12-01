from django.db import models
from accounts.models import Profile, Notification
# Create your models here.


class Relation(models.Model):
    from_user = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL, related_name="from_user")
    to_user = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL, related_name="to_user")
    relations = ((0, 'neutral'),
                (1, 'friend'),
                (2, 'friend_request'),
                (3, 'blocked'),
                # (4, 'blocked_by'),
                )
    relation = models.IntegerField(choices=relations, default=0)
    
    def create_relation(self):
        # previous_relation = Relation.objects.get(from_user=self.from_user, to_user=self.to_user)
        # previous_relation = Relation.objects.get(from_user=self.to_user, to_user=self.from_user)
        self.save()
        notif = Notification(user=self.to_user.user, message=f'{self.from_user} want s to be your friend')
        notif.save()
    
    def __str__(self):
        return f'{self.from_user} is {self.relation} with {self.to_user}'