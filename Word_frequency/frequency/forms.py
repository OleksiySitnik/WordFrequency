from django import forms

from frequency.models import Text


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Text
        fields = ('text',)