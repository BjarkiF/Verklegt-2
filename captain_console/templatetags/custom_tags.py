from django import template
from config.models import Config
from django.conf import settings
register = template.Library()

@register.simple_tag
def footer_email():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('email').last()[0]

@register.simple_tag
def footer_telephone():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('telephone').last()[0]

@register.simple_tag
def footer_address():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('address').last()[0]

@register.simple_tag
def footer_hours_weekdays():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('hours_weekdays').last()[0]

@register.simple_tag
def footer_hours_saturday():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('hours_saturday').last()[0]

@register.simple_tag
def footer_hours_sunday():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('hours_sunday').last()[0]


@register.simple_tag
def footer_social_instagram():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('social_instagram').last()[0]


@register.simple_tag
def footer_social_facebook():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('social_facebook').last()[0]


@register.simple_tag
def footer_social_twitter():
    """Removes all values of arg from the given string"""
    return Config.objects.values_list('social_twitter').last()[0]
