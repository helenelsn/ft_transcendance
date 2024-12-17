from django import template
register = template.Library()
from common.templatetags.tags_utils import topnav_hyperlinks
from common.templatetags.html_utils import simple_redir_list, index_hyperlink, a_hyperlink, html_list_join
from common.templatetags import html_utils
from accounts.model_view import AccountsAppView
# from relationship.templatetags.relation_tags import relation_actions
from accounts.models import User, Profile

app_name='accounts'

from notifications.templatetags import notif_tags


@register.simple_tag
def accounts_managment_links(user):
    return AccountsAppView().get_app_redirs(user=user).html_one_line

@register.simple_tag
def account_index_hyperlink():
    return index_hyperlink(app_name)
    
@register.simple_tag
def account_edit_hyperlink(user):
    return a_hyperlink(f'{app_name}:edit_profil', 'edit', args=[user.id])
    

@register.simple_tag
def profil_detail_menu(request, obj):
    if request.user == obj:
        return html_list_join([ topnav_hyperlinks(request.user, as_p=True ), account_edit_hyperlink(request.user) ], as_p=True)
