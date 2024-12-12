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
def format_hyperlink(link, display, ):
    return format_html(f'<a href={link}> {display} </a>')

@register.simple_tag
def a_hyperlink(redir, display, args=None,):
    return format_html(f'<a {ref(redir, args)}> {display} </a>')

def format_p(content):
    return format_html(f'<p>{content}</p>')


def index_hyperlink(app_name, display=None):
    if display==None:
        display = app_name
    return a_hyperlink(f'{app_name}:index', display)

def simple_redir_list(redirs, as_p=False):
    return html_list_join([a_hyperlink(key, redirs[key]) for key in redirs], as_p=as_p)

def same_arg_redir_list(redirs, args, sep='', as_p=False):
    return html_list_join([a_hyperlink(key, redirs[key], args=args) for key in redirs], sep=sep, as_p=as_p)

def html_list_join(lst, sep='', as_p=False, as_li=False):
    if as_p:
        lst = [f'<p>{elem}</p>' for elem in lst]
    elif as_p:
        lst = [f'<li>{elem}</li>' for elem in lst]
    return format_html(sep.join(lst))

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

