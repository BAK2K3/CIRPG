from django import forms
from .models import Codex
from .widgets import CustomClearableFileInput


class CodexForm(forms.ModelForm):

    class Meta:
        model = Codex
        fields = '__all__'

    image = forms.ImageField(label="Image", required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super(CodexForm, self).__init__(*args, **kwargs)
