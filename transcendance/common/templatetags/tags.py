from django import template
from .tags_utils import html_list_join, simple_redir_list
from accounts.templatetags.accounts_tags import accounts_managment_links
register = template.Library()


@register.simple_tag
def sidenav_hyperlinks(user):
    redirs = {
        'games:index':  'Games',
        'accounts:index': 'Accounts',
    }
    if user.is_authenticated: 
        redirs.update({
            'tournaments:index': 'Tournaments',
            'relationship:index': 'All',
            'notifications:index': 'Notif',
        })
    return html_list_join([accounts_managment_links(user), simple_redir_list(redirs)] )
    
    