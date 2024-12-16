from django import template
register = template.Library()
from common.templatetags.tags_utils import menu_hyperlinks
from common.templatetags.html_utils import simple_redir_list, index_hyperlink, a_hyperlink, html_list_join
from common.templatetags import html_utils

# from relationship.templatetags.relation_tags import relation_actions
from accounts.models import User, Profile

app_name='accounts'

from notifications.templatetags import notif_tags
@register.simple_tag
def accounts_managment_links(user):
    if user.is_authenticated: 
        redirs = {
            'accounts:index': f'{user.username}',
            'accounts:logout': 'logout',
        }
        if len(notif_tags.get_unreads(user))>0:
            redirs.update({'notifications:index':'New notif!'})
    else:
        redirs = {
            'accounts:login': 'login',
            'accounts:register': 'register',
        }
    return simple_redir_list(redirs)

@register.simple_tag
def account_index_hyperlink():
    return index_hyperlink(app_name)
    
@register.simple_tag
def account_edit_hyperlink(user):
    return a_hyperlink(f'{app_name}:edit_profil', 'edit', args=[user.id])
    

@register.simple_tag
def profil_detail_menu(request, obj):
    if request.user == obj:
        return html_list_join([ menu_hyperlinks(request.user, as_p=True ), account_edit_hyperlink(request.user) ], as_p=True)
    # else:
    #     return relation_actions(request.user.profile, obj)

@register.simple_tag
def  profil_detail_link(profil):
    if isinstance(profil, User):
        profil = profil.profile
    return html_utils.format_hyperlink(profil.get_absolute_url(), profil.user.username)