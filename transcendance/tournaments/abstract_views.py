from django.shortcuts import render, get_object_or_404, redirect
from .models import Tournament
from django.urls import reverse
from common.templatetags import html_utils

app_name = 'tournaments'

class TournamentView():
    def __init__(self, tournament : Tournament):
        self.tournament=tournament
        
    def get_edit_url(self):
        return reverse('tournaments:tournament_settings', args=[self.tournament.pk])
    
    @property
    def linked_name(self):
        return html_utils.format_hyperlink(link=self.tournament.get_absolute_url(), display=self.tournament.name)

    def get_actions(self, user):
        actions = {}
        # if not self.tournament.is