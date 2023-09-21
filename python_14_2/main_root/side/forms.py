from django import forms


class LogInForm(forms.Form):
    login = forms.CharField(label='login', max_length=25, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput(), required=False)