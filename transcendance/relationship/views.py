from typing import Any
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .model_view import RelationView
from .tables import RelationTable, FriendGameInviteTable
from .models import Relation
from .filters import RelationFilter, FriendFilter
from accounts.models import User
from .models import NEUTRAL, REQUEST, FRIEND, BLOCKED

@login_required
def index(request):    
    return render(request, "relationship/index.html", {})

@login_required
def relation_list(request):
    filter = RelationFilter(request.GET, request=request, queryset=Relation.objects.all())
    table = RelationTable(data=filter.qs, request=request)
    return render(request, 'relationship/relation_list.html', {'filter': filter, 'table':table})

def game_invite_view(request, game):
    f = FriendFilter(request.GET, request=request, queryset=Relation.objects.all())
    table = FriendGameInviteTable(data=f.qs, game=game, request=request)
    return render(request, 'relationship/relation_list.html', {'filter': f, 'table':table})
     
@login_required
def detail(request, pk):
    obj = Relation.objects.get(pk=pk)
    return RelationView(obj).detail_view()

@login_required
def to_neutral(request, pk):
    return RelationView(request=request, pk=pk).update_relation(NEUTRAL)

@login_required
def to_request(request, pk):
    return RelationView(request=request, pk=pk).update_relation(REQUEST)
    
@login_required
def to_friend(request, pk):
    return RelationView(request=request, pk=pk).update_relation(FRIEND)
    
@login_required
def to_block(request, pk):
    return RelationView(request=request, pk=pk).update_relation(BLOCKED)
