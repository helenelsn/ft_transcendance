from django import template
from django.utils.html import format_html
from django.urls import reverse

register = template.Library()

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

@register.inclusion_tag('utils/table.html', takes_context=True)
def include_filter_table(context, table, table_title='', filter=None):
    context.update({'table':table,
            'table_title':table_title})
    return context

# @register.inclusion_tag('common/g_base.html', takes_context=True)
# def extend_base(context, content):
#     context['content'] = content
#     return context