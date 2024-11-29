from django.contrib import admin
from .models import Tournament, TournamentPlayer
# Register your models here.
admin.site.register(TournamentPlayer)
admin.site.register(Tournament)