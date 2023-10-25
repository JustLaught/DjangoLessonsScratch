from django import forms


class RestRegForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, required=True)
    spec = forms.ChoiceField(label='Specification', choices=[('Italian', 'Italian'), ('French', 'French'), ('Family', 'Family'), ('Bulgarian', 'Bulgarian'), ('Ukrainian', 'Ukrainian')], required=True)
    address = forms.CharField(label='Address', max_length=70, required=True)
    web_site = forms.CharField(label='Website', max_length=70, required=True)
    phone = forms.CharField(label='Contact phone', max_length=50, required=True)