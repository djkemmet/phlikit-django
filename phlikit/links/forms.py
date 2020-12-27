from django import forms
from .models import ShortenedLink


class LinkShorteningForm(forms.ModelForm):
    link = forms.URLField(help_text='Enter the link you want shortened')
    shortened_result = forms.URLField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = ShortenedLink
        fields = ['link', ]