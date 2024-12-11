from django.contrib import admin

from .models import Game, GameInvitation
# Register your models here.
admin.site.register(Game)
admin.site.register(GameInvitation)