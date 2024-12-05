from django import template
register = template.Library()
from common.templatetags.tags_utils import simple_redir_list, index_hyperlink, a_hyperlink,menu_hyperlinks, html_list_join
from relationship.templatetags.relation_tags import relation_actions
app_name='accounts'

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

@register.simple_tag
def account_index_hyperlink():
    return index_hyperlink(app_name)
    
@register.simple_tag
def account_edit_hyperlink(user):
    return a_hyperlink(f'{app_name}:edit_profil', 'edit', args=[user.id])
    

@register.simple_tag
def profil_detail_menu(request, obj):
    if request.user == obj:
        menu_hyperlinks(request.user)
        return html_list_join([ menu_hyperlinks(request.user), account_edit_hyperlink(request.user) ])
    else:
        return relation_actions(request.user.profile, obj)