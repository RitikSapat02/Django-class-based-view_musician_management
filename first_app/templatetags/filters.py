from django import template

register = template.Library()           #define template library

def my_filter(value):
    return value + " This is a string from custom filter"

register.filter('custom_filter',my_filter)