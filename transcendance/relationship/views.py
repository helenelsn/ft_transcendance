from typing import Any
from django.shortcuts import render
from .abstract_view import RelationView
from django.http import Http404
from .tables import RelationTable, FriendGameInviteTable
from .models import Relation
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import RelationFilter, FriendFilter
from accounts.models import User
@login_required
def index(request):
    
    return render(request, "relationship/index.html", {})
 
class RelationListView(SingleTableMixin, FilterView):
    table_class = RelationTable
    model = Relation
    template_name = "relationship/relation_list.html"

    filterset_class = RelationFilter
    

def game_invite_view(request, game):
    f = FriendFilter(request.GET, request=request, queryset=Relation.objects.all())
    table = FriendGameInviteTable(data=f.qs, game=game, request=request)
    return render(request, 'relationship/relation_list.html', {'filter': f, 'table':table})


class FriendGameInviteListView(RelationListView):
    
    filterset_class = FriendFilter
    table_class = FriendGameInviteTable
    
    
    