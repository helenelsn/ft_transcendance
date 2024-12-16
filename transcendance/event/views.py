from django.shortcuts import render
from common.templatetags import html_utils
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from abc import ABC, abstractmethod
from .models import Event, models, User, EventInvitation
from .model_view import EventView
from games.models import Game

@login_required
def create_event(request):
    return EventView.create(request.user)

@login_required
def register_event(request, pk):
    return EventView(object=pk).register_player(request.user)

@login_required
def unregister_event(request, pk):
    return EventView(pk).unregister_player(request.user)

@login_required 
def delete_event(request, pk):
    return EventView(pk).delete()

@login_required
def invite_to_event(request, pk, player_pk):
    return EventView(pk).invite_player(player_pk)

@login_required
def event_detail(request, pk):
    if Game.objects.get(pk=pk) is not None:
        return redirect(Game.objects.get(pk=pk))