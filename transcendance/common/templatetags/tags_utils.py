from django import template
from django.utils.html import format_html
from django.urls import reverse

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
def ref(redir, args=None):
    if args is not None and not isinstance(args, list):
        args = [args]
    return format_html(f'href={reverse(f"{redir}", args=args)}')

@register.simple_tag
def a_hyperlink(redir, display, args=None,):
    return format_html(f'<a {ref(redir, args)}> {display} </a>')

def index_hyperlink(app_name, display=None):
    if display==None:
        display = app_name
    return a_hyperlink(f'{app_name}:index', display)

def simple_redir_list(redirs):
    return html_list_join([a_hyperlink(key, redirs[key]) for key in redirs])

def same_arg_redir_list(redirs, args, sep=''):
    return html_list_join([a_hyperlink(key, redirs[key], args=args) for key in redirs], sep)

def html_list_join(lst, sep=''):
    return format_html(''.join(lst))

@register.simple_tag
def get_obj_attr(o, attribut_name):
    return getattr(o, attribut_name)

@register.inclusion_tag('utils/table.html', takes_context=True)
def include_table(context, table, table_title=''):
    context.update({'table':table,
            'table_title':table_title})
    return context

@register.inclusion_tag('utils/table.html', takes_context=True)
def include_table(context, table, table_title=''):
    context.update({'table':table,
            'table_title':table_title})
    return context

@register.inclusion_tag('utils/filter_table.html', takes_context=True)
def include_filter_table(context, table, table_title='', filter=None):
    context.update({
            'filter':filter,
            'table':table,
            'table_title':table_title
        })
    return context


@register.simple_tag
def menu_hyperlinks(user):
    redirs = menu_redir_glob
    if user.is_authenticated: 
        redirs.update(menu_redir_authenticate)
    return simple_redir_list(redirs)
