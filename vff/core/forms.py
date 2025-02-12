from django import forms

class MarvelForm(forms.Form):
    first_name = forms.CharField()

    def clean_first_name(self):
        validate_name = self.cleaned_data['first_name']

        if len(validate_name)<5:
            raise forms.ValidationError('please enter name greater than 5 letters')