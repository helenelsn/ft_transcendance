from django import template
from django.utils.html import format_html
from django.urls import reverse
from common.templatetags.html_utils import simple_redir_list

register = template.Library()

menu_redir_authenticate = {
            # 'accounts:index': 'my profile',
            'notifications:index': 'notif',
            'relationship:index': 'relations',
            'tournaments:index': 'tournaments',
        }

menu_redir_glob = {
    'games:index':  'games',
}



@register.simple_tag
def menu_hyperlinks(user, as_p=False):
    redirs = menu_redir_glob
    if user.is_authenticated: 
        redirs.update(menu_redir_authenticate)
        # html_utils.
    return simple_redir_list(redirs, as_p=as_p)
