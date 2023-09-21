from django import forms

class AddContact(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    lastname = forms.CharField(label='LastName', max_length=30)
    email = forms.EmailField(label='Email', max_length=254)
    phone = forms.CharField(label='Phone', max_length=18)
    about = forms.CharField(label='About', max_length=150)