from django import forms
from django.core import validators

class CompForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20, required=True, validators=[validators.RegexValidator(regex='\w*')])
    lastname = forms.CharField(label='LastName', max_length=20, required=True, validators=[validators.RegexValidator(regex='\w*')])
    phone = forms.CharField(label='Phone', max_length=16, required=True)
    email = forms.EmailField(label='Email', required=True)
    prop_name = forms.CharField(label='ProductName', max_length=40, required=True)
    bouth_date = forms.DateField(label="BouthDate", required=True)
    description = forms.CharField(label='Description', max_length=5000, required=True, widget=forms.Textarea())