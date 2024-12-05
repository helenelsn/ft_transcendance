from django.shortcuts import render
from .abstract_view import RelationView
from django.http import Http404
from .tables import RelationTable
from .models import Relation
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import RelationFilter

@login_required
def index(request):
    return render(request, "relationship/index.html", {})
 
class RelationListView(SingleTableMixin, FilterView):
    table_class = RelationTable
    model = Relation
    template_name = "relationship/manage.html"

    filterset_class = RelationFilter
    


