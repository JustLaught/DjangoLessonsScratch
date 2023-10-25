from django import forms

class SiteForm(forms.Form):
    nickname = forms.CharField(label='NickName', max_length=30, required=True)
    email = forms.EmailField(label='Email', required=True)
    rating = forms.ChoiceField(label='Rating', choices=[(1,'Poor'), (2, 'Not Bad'), (3, 'Solid'), (4, 'Lit'), (5, 'Incredible')], required=True)
    description = forms.CharField(label='Description', max_length=300, required=True)

class RewievForm(forms.Form):
    nickname = forms.CharField(label='NickName', max_length=30, required=True)
    rating = forms.IntegerField(label='Rating',min_value=1, max_value=100, required=True)
    review = forms.CharField(label='Rewiev', max_length=300, required=True)
    spoilers = forms.BooleanField(label='Spoilers', required=True)