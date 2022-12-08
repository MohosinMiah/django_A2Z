from django import forms
from django.core.exceptions import ValidationError

class ArticalForm(forms.Form):
    title = forms.CharField(label='Your Artical Title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title'].upper()
        return title

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title').upper()
        return cleaned_data