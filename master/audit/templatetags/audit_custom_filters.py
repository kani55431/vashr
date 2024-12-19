# In your custom_filters.py or similar file
from django import template
from django.utils.translation import gettext_lazy as _
from django import template

register = template.Library()

@register.filter
def time_duration(value):
    """Formats a timedelta duration to HH:MM format"""
    if isinstance(value, datetime.timedelta):
        total_seconds = int(value.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f'{hours:02}:{minutes:02}'
    return value






@register.filter(name='intword')
def intword(value):
    try:
        # Convert the value to an integer if it is a float or string that represents a number
        if isinstance(value, (int, float)):
            return p.number_to_words(int(value))
        elif isinstance(value, str) and value.isdigit():
            return p.number_to_words(int(value))
        return value
    except Exception as e:
        # Handle the error and return a friendly message
        return f"Error: {e}"