from django import template
register = template.Library()


@register.filter
def get_msg(error_dict):
    if error_dict.get('__all__'):
        return error_dict.get('__all__')[0]


