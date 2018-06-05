from django import template
register = template.Library()


@register.simple_tag
def get_error(error_dict):
    return error_dict.get('__all__')


