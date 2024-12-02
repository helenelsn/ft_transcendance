from django.contrib import admin

# Register your models here.
from .models import Relation, FriendInvitation
# Register your models here.
admin.site.register(Relation)
admin.site.register(FriendInvitation)