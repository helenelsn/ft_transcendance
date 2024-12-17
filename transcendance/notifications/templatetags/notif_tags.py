from django import template
from common.templatetags import html_utils
from django.utils.html import format_html
from notifications.models import Notification
from notifications.tables import NotificationTable
register = template.Library()


@register.simple_tag
def get_unreads(user):
    return user.notification_set.order_by('-timestamp').filter(is_read=False).all()

from notifications.views  import NotificationsView

@register.simple_tag
def all_notif_actions(user):
    return NotificationsView(user=user).get_actions_on_all()

@register.simple_tag
def notif_actions(notif):
    return NotificationsView.notif_actions(notif, as_p=True)
    
# @register.simple_tag
# def user_unread_notif(user, ):
#     if len(get_unreads(user)) > 0:
#         return html_utils.a_hyperlink(redir='notifications:index', display='NewNotif!')