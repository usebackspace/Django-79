from django import forms

class MarvelForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

        
    def clean(self):
        cleaned_data= super().clean()

        val_pass = cleaned_data['password']
        val_conpass = cleaned_data['confirm_password']

        if val_pass!=val_conpass:
            raise forms.ValidationError('Password doen"t match')
        
        val_fname = cleaned_data['first_name']
        if len(val_fname)<5:
            raise forms.ValidationError('Please enter name letter more than 5')
        

    