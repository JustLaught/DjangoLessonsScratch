from django.shortcuts import render
from .forms import RegForm

# Create your views here.

def index3(request):
    form = RegForm()
    upform = RegForm(request.POST)
    if request.method == 'POST' and upform.is_valid():
        data = {
            'Name': upform.cleaned_data['name'],
            'LastName': upform.cleaned_data['lastname'],
            'Age': upform.cleaned_data['age'],
            'Email': upform.cleaned_data['email'],
            'Gender': upform.cleaned_data['gender'],
            'Addres': upform.cleaned_data['addres'],
        }
        return render(request, 'message.html', {'data': data})
    
    return render(request, 'index3.html', {'form': form})