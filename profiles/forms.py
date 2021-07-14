from django import forms


class HiddenForm(forms.Form):
    user_selection = forms.CharField()
