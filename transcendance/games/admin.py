from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Game)
admin.site.register(GameHistory)
admin.site.register(GameLaunching)
admin.site.register(GameInvitation)