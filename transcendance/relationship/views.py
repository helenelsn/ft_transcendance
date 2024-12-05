from django.shortcuts import render, get_object_or_404, redirect 
from django_tables2 import  SingleTableMixin
from .abstract_view import RelationView
from django.http import Http404
app_name = 'relationship'
from .tables import RelationTable
from .models import Relation
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    return render(request, "relationship/index.html", {})

ALL=5

def render_relation_table(request, rel_key):
    set = Relation.objects.filter(from_user=request.user).order_by('relation')
    if rel_key == 'all':
        pass
    elif int(rel_key) in Relation.relations:
        set = set.filter(relation=int(rel_key))
    else:
        raise Http404()
    table = RelationTable(set.all(), request=request)
    return render(request, "relationship/all.html", {
        "table": table
    })

@login_required
def all(request):
    table = RelationTable(Relation.objects.filter(from_user=request.user).order_by('relation').all(), request=request)
    return render(request, "relationship/all.html", {
        "table": table
    })
    

