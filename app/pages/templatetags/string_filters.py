from django import template

register = template.Library()


@register.filter
def space(value, arg = '_'):
    """
    Replace passed character on space character
    Use `{{ "a_a"|space }}`
    """

    return value.replace(arg, ' ')
