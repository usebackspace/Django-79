from django import forms
from . models import MarvelModel
# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()


class MarvelForm(forms.ModelForm):

    class Meta:
        model = MarvelModel
        # fields='__all__'
        fields=['name','heroic_name']