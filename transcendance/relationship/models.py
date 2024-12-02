from typing import Any
from django.db import models
from accounts.models import Profile
from notifications.models import Notification
# Create your models here.


NEUTRAL = 0
FRIEND = 1
REQUEST = 2
BLOCKED = 3

class Relation(models.Model):
    from_user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name="from_user")
    to_user = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE, related_name="to_user")
    relations = (
                (NEUTRAL, 'neutral'),
                (FRIEND, 'friend'),
                (REQUEST, 'friend_request'),
                (BLOCKED, 'blocked'),
                )
    relation = models.IntegerField(choices=relations, default=0)
    
    def create_request(self):
        self.change_relation(REQUEST)
        self.send_notif()
        
    def get_or_create_other_pov(self):
        rel, created = Relation.objects.get_or_create(from_user=self.to_user, to_user=self.from_user) 
        return rel
    
    def send_notif(self):
        if not self.is_bloqued():
            message=f'{self}'
            if self.relation == REQUEST:
                notif = FriendInvitation(user=self.to_user.user, message=message, relation=self)
            else:
                notif = Notification(user=self.to_user.user, message=message)
                
            notif.save()
            # self.notifications.add(notif)
            # self.save()
    
    def send_notif_to_both(self):
        self.send_notif()
        self.get_or_create_other_pov().send_notif()
        
    def change_relation(self, type):
        self.relation = type
        self.save()
        
    def change_both_relations(self, type):
        self.change_relation(type)
        self.get_or_create_other_pov().change_relation(type)
        
    def becaming_friend(self):
        self.change_both_relations(FRIEND)
        self.send_notif_to_both()
        
    def unfriend(self):
        self.change_both_relations(NEUTRAL)
        self.send_notif_to_both()
        
    def block_user(self):
        self.change_relation(BLOCKED)
        self.send_notif()
        
    def is_bloqued(self):
        other_pov = self.get_or_create_other_pov()
        return other_pov is not None and other_pov.relation == BLOCKED
        
    def update_relation(self, from_user, to_user, type):
        rel, created = Relation.objects.filter(from_user=from_user).filter(to_user=to_user).get_or_create()
        if created:
            rel.to_user = to_user
            rel.from_user = from_user
        if rel.from_user == rel.to_user:
            return
        if type == REQUEST:
            rel.create_request()
        elif type == FRIEND:
            rel.becaming_friend()
        elif type == BLOCKED:
            rel.block_user()
        elif type == NEUTRAL:
            rel.unfriend
        
    
    def __str__(self):
        if self.relation == REQUEST:
            mess = "want s to be friend with"
        if self.relation == NEUTRAL:
            mess = "is neurtal about"
        if self.relation == FRIEND:
            mess = "is friend with"
        if self.relation == BLOCKED:
            mess = "blocked"
        return f'{self.from_user} {mess} {self.to_user}'
    
    
class FriendInvitation(Notification):
    relation = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    
    def accept(self):
        pass
        
    
    def actions(self):
        return

        