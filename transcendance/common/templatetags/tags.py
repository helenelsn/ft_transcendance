from django import template

register = template.Library()

@register.simple_tag
def get_obj_attr(o, attribut_name):
    return getattr(o, attribut_name)


