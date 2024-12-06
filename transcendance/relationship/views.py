from django.shortcuts import render
from .abstract_view import RelationView
from django.http import Http404
from .tables import RelationTable
from .models import Relation
from django.contrib.auth.decorators import login_required
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import RelationFilter
from accounts.models import User
@login_required
def index(request):
    existing_relationhip = Relation.objects.filter(from_user=request.user)
    if len(existing_relationhip) < len(User.objects.all()) - 1:
        for user in User.objects.exclude(id__in=existing_relationhip.select_related('to_user')).all():
            Relation().update_relation(from_user=request.user, to_user=user, )
    return render(request, "relationship/index.html", {})
 
class RelationListView(SingleTableMixin, FilterView):
    table_class = RelationTable
    model = Relation
    template_name = "relationship/relation_list.html"

    filterset_class = RelationFilter
    


