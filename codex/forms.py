from django import forms
from .models import Codex
from .widgets import CustomClearableFileInput


class CodexForm(forms.ModelForm):
    """
    Form for the Codex Model.

    Uses custom clearable file input
    due to the ability to extract the
    image location via the widget.
    """

    class Meta:
        model = Codex
        fields = '__all__'

    image = forms.ImageField(label="Image", required=False,
                             widget=CustomClearableFileInput)
