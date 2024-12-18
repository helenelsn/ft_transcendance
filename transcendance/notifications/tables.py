import django_tables2 as tables
from accounts.models import Profile, User
from .models import Notification 
from django.utils.html import format_html
from django.urls import reverse
from django_tables2.columns.linkcolumn import BaseLinkColumn, LinkColumn
from relationship.models import FriendInvitation
from common.templatetags import html_utils
from .model_view import NotificationsView
from common.tables import ActionsColumn

class NotificationTable(tables.Table):
    message = tables.Column()
    delete = tables.Column(empty_values=[])
    react = ActionsColumn()
    
    class Meta:
        model = Notification
        fields = ( 'message', 'timestamp', 'is_read')
        
    def render_message(self, value, record):
        return NotificationsView(record).detail_linked_name
        
    def render_is_read(self, record, value):
        return NotificationsView(record).is_read_action().get_html
        
    def render_delete(self, record):
        return NotificationsView(record).delete_action().get_html
        
    # def render_react(self, record):
    #     return NotificationsView.notif_react_action(record)