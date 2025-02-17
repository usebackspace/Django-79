from django import forms
from . models import MarvelModel
# class MarvelForm(forms.Form):
#     name = forms.CharField()
#     heroic_name = forms.CharField()


class MarvelForm(forms.ModelForm):
    name = forms.CharField(max_length=30) # This field has highest priority compare to the field defined in marvel model.

    class Meta:
        model = MarvelModel
        # fields='__all__'
        fields=['name','heroic_name']
        labels ={
            'name':'Full Name'
        }
        error_messages ={
            'name':{'required':'Enter name properly'},
            'heroic_name':{'required':'Enter heroic name properly'},
        }
        widgets={
            # 'name':forms.PasswordInput()
            # 'heroic_name':forms.TextInput(attrs={'class':'form-control'})
        }