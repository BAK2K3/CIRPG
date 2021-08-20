"""
Codex App - Widgets
----------------

Custom HTML Widgets for Codex App.
    - CustomClearableFileInput

"""

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom ClearableFileInput widget to specify initial text,
    input text, and custom HTML template.
    """
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'codex/custom_widget_templates/custom_clearable_file_input.html'
    )
