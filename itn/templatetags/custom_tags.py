from django import template

register = template.Library()

@register.simple_tag
def unslugfy(value):
    try:
        return value.replace('_', ' ').title()
    except:
        return value