from django import template
register = template.Library()
from common.templatetags.tags_utils import simple_redir_list

@register.simple_tag
def accounts_managment_links(user):
    if user.is_authenticated: 
        redirs = {
            'accounts:index': 'my profile',
            'accounts:logout': 'logout',
        }
    else:
        redirs = {
            'accounts:login': 'login',
            'accounts:logout': 'logout',
        }
    return simple_redir_list(redirs)
