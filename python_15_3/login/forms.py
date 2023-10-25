from django import forms


class LogIN(forms.Form):
    name = forms.CharField(label='name', max_length=25, required=True)
    password = forms.CharField(label='password', max_length=25, required=True, widget=forms.PasswordInput())


class Register(forms.Form):
    name = forms.CharField(label='name', max_length=25, required=True)
    password = forms.CharField(label='password', max_length=25, required=True, widget=forms.PasswordInput())
    superuser = forms.BooleanField(label='superuser', required=False, widget=forms.CheckboxInput())