from django import template

register = template.Library()


@register.filter(name='split')
def split(values, key, text=None):
    for value in values:
        text = value.split(key)
    return text
