from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def company_name():
    return settings.COMPANY_NAME

@register.inclusion_tag('arrow_temp.html', takes_context=True)
def find_arrow(context, field_to_sort_tag):
    return {'direction_to_sort': context['direction_to_sort'],
            'field_to_sort': context['field_to_sort'],
            'field_to_sort_tag': field_to_sort_tag}