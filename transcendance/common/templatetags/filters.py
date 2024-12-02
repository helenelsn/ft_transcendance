from django import template

register = template.Library()

@register.filter(name='dict_val')
def dict_val(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]

@register.filter()
def app_redir(app_name :str, redir:str):
    return f'{app_name}:{redir}'

@register.filter()
def index_redir(app_name :str):
    return f'{app_name}:index'

