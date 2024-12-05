from django import template
register = template.Library()


@register.simple_tag
def get_short_unread(user):
    return user.notification_set.order_by('-timestamp').filter(is_read=False)[:3]

from notifications.views import NotificationsView
@register.simple_tag
def generic_actions_names():
    return NotificationsView.get_generic_actions_names()

@register.simple_tag
def generic_actions(notif):
    return NotificationsView().get_generic_actions(notif)

@register.simple_tag
def global_actions():
    return NotificationsView.get_global_actions()