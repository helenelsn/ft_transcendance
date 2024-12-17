from django.shortcuts import render, get_object_or_404
from common.utils import get_action_table_context, get_context
from relationship.models import FriendInvitation
from django.contrib.auth.decorators import login_required
from common.utils import redir_to_index, redir_to
from typing import Any
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic import ListView, DetailView

from .models import Notification
from .model_view import NotificationsView
from .tables import NotificationTable
from .filters import NotificationFilter
from common.templatetags import html_utils
app_name = 'notifications'

class NotificationsDetailsView(DetailView):
    model = Notification
    template_name = "notifications/notification_detail.html"
    

class NotificationsListView(SingleTableMixin, FilterView):
    table_class = NotificationTable
    model = Notification
    template_name = "notifications/notification_list.html"
    filterset_class = NotificationFilter




    