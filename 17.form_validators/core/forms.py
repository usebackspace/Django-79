from django import forms
from django.core import validators

def start_with_a(val):
    x= val[0]
    print(x)
    if x.isdigit():
        raise forms.ValidationError('Please start name with letter not number ')


class MarvelForm(forms.Form):
    first_name = forms.CharField(validators=[start_with_a])
    last_name = forms.CharField(validators=[validators.MaxLengthValidator(4)])


