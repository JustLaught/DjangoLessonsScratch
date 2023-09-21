from django.core import validators
from django import forms

class AdvForm(forms.Form):
    name = forms.CharField(max_length=20, required=False)
    surname = forms.CharField(max_length=20, required=False)
    age = forms.IntegerField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=[(1,'Male'), (2,'Female')])