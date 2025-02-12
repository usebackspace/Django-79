from django import forms

class MarvelForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(error_messages={'required':'hello'})

    # def clean_first_name(self):
    #     validate_name = self.cleaned_data['first_name']

    #     if len(validate_name)<5:
    #         raise forms.ValidationError('please enter name greater than 5 letters')
        
    # def clean_last_name(self):
    #     validate_name = self.cleaned_data['last_name']

    #     if len(validate_name)>5:
    #         raise forms.ValidationError('please enter name greater than 5 letters')
        

    def clean(self):
        cleaned_data = super().clean()

        val_fname= cleaned_data['first_name']
        val_lname= cleaned_data['last_name']

        if len(val_fname)>5:
            raise forms.ValidationError('please enter name greater than 5 letters')
        
        if len(val_lname)<5:
            raise forms.ValidationError('please enter name greater than 5 letters')