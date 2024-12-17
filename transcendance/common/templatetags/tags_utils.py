from django import template
from django.utils.html import format_html
from django.urls import reverse
from common.templatetags.html_utils import simple_redir_list
from common import global_view_mananger
register = template.Library()

@register.simple_tag
def topnav_hyperlinks():
    return global_view_mananger.get_apps_topnav_hyperlinks()

@register.simple_tag
def sidenav_hyperlinks(user):
    return global_view_mananger.get_apps_sidenav_hyperlinks(user)