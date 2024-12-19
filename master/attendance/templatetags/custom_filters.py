from django import template

register = template.Library()

@register.filter
def dict_key(value, arg):
    """Custom filter to access a dictionary by key."""
    return value.get(arg)




@register.filter
def add(value, increment):
    """Add a value to the given number."""
    try:
        return int(value) + int(increment)
    except (ValueError, TypeError):
        return value
