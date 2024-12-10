from accounts.models import User, Profile
from relationship.models import Relation, FRIEND, REQUEST
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        self.populate_user()
        self.personalised_profil()
        self.create_relationships()
    
    def populate_user(self):
        for i in range(100):
            User.objects.create_user(username=f'user{i}',
                                        password=f'ViveLeVent{i}',)
        User.objects.create_superuser(username='super', password='super')
        User.objects.create_superuser(username='lol',password='lol' )
            
    def personalised_profil(self):
        
        for profil in Profile.objects.all():
            profil.bio = f'wonderfull bio of {profil.user.username}'
            profil.save()
            
    def create_relation(self, from_user, to_user, friend=True):
        if friend:
            Relation().update_relation(from_user=from_user.user, to_user=to_user.user, type=FRIEND)
        else:
            Relation().update_relation(from_user=from_user.user, to_user=to_user.user, type=REQUEST)
            
    def create_relationships(self):
        for k in range( 8, 10):
            for i in range(10):
                pi = Profile.objects.filter(user__username=f'user{k}{i}').get()
                
                pj = Profile.objects.filter(user__username=f'super').get()
                self.create_relation(pi, pj, friend=False)
                pj = Profile.objects.filter(user__username=f'lol').get()
                self.create_relation(pi, pj, friend=False)
                
                for j in range(30):
                    pj = Profile.objects.filter(user__username=f'user{j}').get()
                    self.create_relation(pi, pj, friend=False)
                
                
        #create friendship relation between all player
        for i in range(10):
            pi = Profile.objects.filter(user__username=f'user{i}').get()
            
            pj = Profile.objects.filter(user__username=f'super').get()
            self.create_relation(pi, pj)
            pj = Profile.objects.filter(user__username=f'lol').get()
            self.create_relation(pi, pj)
            
            for j in range(1, 10):
                pj = Profile.objects.filter(user__username=f'user{j}{i}').get()
                self.create_relation(pi, pj)
    
        for user in User.objects.all():
            existing_relationhip = Relation.objects.filter(from_user=user)
            if len(existing_relationhip) < len(User.objects.all()) - 1:
                for user in User.objects.exclude(id__in=existing_relationhip.select_related('to_user')).all():
                    Relation().update_relation(from_user=user, to_user=user, )
        