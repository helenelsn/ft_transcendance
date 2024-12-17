from django import template
from django.utils.html import format_html
from django.urls import reverse
from common.templatetags.html_utils import simple_redir_list
from common import global_view_mananger
register = template.Library()

menu_redir_authenticate = {
            # 'accounts:index': 'my profile',
            'notifications:index': 'notif',
            'relationship:index': 'relations',
            # 'tournaments:index': 'tournaments',
        }

menu_redir_glob = {
    # 'games:index':  'games',
}

# @register.simple_tag
# def apps_indexs_hyperlinks(user, as_p=False):
#     indexes = {f'{app_name}:index' : display for app_name, display in {'accounts': 'my profile', 'notifications' : 'notifs', 'relationship' : 'relations',}}
        

@register.simple_tag
def menu_hyperlinks(user, as_p=False):
    redirs = menu_redir_glob
    if user.is_authenticated: 
        redirs.update(menu_redir_authenticate)
        # html_utils.
    return global_view_mananger.get_app_views_index_hyperlinks()
    return simple_redir_list(redirs, as_p=as_p)
