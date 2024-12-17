import django_tables2 as tables
from accounts.models import Profile, User
from .models import Notification 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from .model_view import NotificationsView


class NotificationTable(tables.Table):
    delete = tables.Column(empty_values=[])
    react = tables.Column(empty_values=[])
    
    class Meta:
        model = Notification
        fields = ( 'message', 'timestamp', 'is_read')
        
    def render_message(self, value, record):
        return html_utils.a_hyperlink(redir=f'notifications:show_notif', display=value, args=[record.id])
        
    def render_is_read(self, record, value):
        return NotificationsView.notif_is_read_action(record)
        
    def render_delete(self, record):
        return NotificationsView.notif_delete_action(record)
        
    def render_react(self, record):
        return NotificationsView.notif_react_action(record)