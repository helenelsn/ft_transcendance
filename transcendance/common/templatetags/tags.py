from django import template

register = template.Library()

@register.simple_tag
def get_obj_attr(o, attribut_name):
    return getattr(o, attribut_name)

# @register.simple_tag
# def get_url_with_obj_attr(o, attribut_name):
#     return getattr(o, attribut_name)