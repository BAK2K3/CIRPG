"""
Profiles App - Profile Tools
----------------

Additional TemplateTags for Profiles App:
    - calc_subtotal
"""

from django import template


register = template.Library()


@register.simple_tag(name='percent')
def calc_subtotal(value, val_min, val_max):
    """
    Custom template tage for calulating
    user's XP progress to next level.
    Takes in currenct XP, Min XP, Max XP.

    Divides current - min by max - min to
    obtain relative % progression to next level.
    """
    try:
        percentage = (
            ((int(value) - int(val_min)) / (int(val_max) - int(val_min))) * 100
        )
        return percentage
    except (ValueError, ZeroDivisionError):
        return None
