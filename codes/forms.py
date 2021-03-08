from django import forms
from .models import Codes

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter SMS verfication code')

    class Meta:
        model = Codes
        fields = ('number',)