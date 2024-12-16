from django.contrib import admin

from .models import Relation, FriendInvitation

admin.site.register(Relation)
admin.site.register(FriendInvitation)