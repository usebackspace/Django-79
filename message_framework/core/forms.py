from django import forms
from . models import MarvelModel

class MarvelForm(forms.ModelForm):

    class Meta:
        model = MarvelModel
        fields = '__all__'

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control x'}),
            'heroic_name':forms.TextInput(attrs={'class':'form-control x'})
        }