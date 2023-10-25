from django import forms


class RegForm(forms.Form):
    name = forms.CharField(label='name', max_length=30, required=True)
    lastname = forms.CharField(label='lastname', max_length=30, required=True)
    age = forms.CharField(label='age', max_length=3, required=True, widget=forms.NumberInput())
    email = forms.EmailField(label='email', required=True)
    gender = forms.ChoiceField(label='gender', choices=[("Male", "Male"), ("Female", "Female")], required=False)
    addres = forms.CharField(label='addres', max_length=45, required=True)