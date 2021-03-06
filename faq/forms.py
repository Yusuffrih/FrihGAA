from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = [
            'question', 'answer',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'question': 'question',
            'answer': 'answer',
            }

        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded'
            self.fields[field].widget.attrs['rows'] = '5'
            self.fields[field].label = False
