from django import template
from django.conf import settings
register = template.Library()

@register.simple_tag
def footer_data():
    """Removes all values of arg from the given string"""
    return 'FOOTER DATA!'
