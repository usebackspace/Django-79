from django import forms

class MarvelForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    heroic_name = forms.CharField()