from django import forms

class MarvelForm(forms.Form):
    first_name = forms.CharField(initial='krishna',disabled=True)
    last_name = forms.CharField(label_suffix=' - ',help_text='Enter your full name.',widget=forms.TextInput(attrs={'style': 'color: red;'}))
    heroic_name = forms.CharField(label='your name',error_messages={'required': 'This field is required'})
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your text','class': 'form-control x'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))