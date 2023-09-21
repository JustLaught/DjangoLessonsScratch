from django.core import validators
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True, initial='John Dere', validators=[validators.MaxLengthValidator(10, 'Value is to long')])
    password = forms.CharField(label='Password', max_length=100, required=True, widget=forms.PasswordInput, help_text='password here')
    about = forms.CharField(label='About', max_length=2000, required=False, widget=forms.Textarea)