from django import template

register = template.Library()

@register.filter(name='dict_val')
def dict_val(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]


