from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='times')
def times(n):
    return range(n)


@register.filter(name='filter_range')
def filter_range(n, m):
    return range(n, m)
