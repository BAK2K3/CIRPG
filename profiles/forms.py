"""
Profiles App - Forms
----------------

Forms for Profiles App:
    - HiddenForm
"""

from django import forms


class HiddenForm(forms.Form):
    """
    Creates a single field which is designed
    to be hidden, which is used for passing the
    selected user to a view.
    """
    user_selection = forms.CharField()
