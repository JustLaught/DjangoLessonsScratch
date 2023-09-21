from django.core import validators
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Username', initial='John Dere')
    surname = forms.CharField(label='Surname')

class UsNum(forms.Form):
    first=forms.IntegerField()
    second=forms.IntegerField()