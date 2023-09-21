from django.shortcuts import render
from .forms import CompForm

# Create your views here.

def index(request):
    c_form = CompForm(request.POST)
    if request.method == 'POST' and c_form.is_valid():
        data = {
            'Name': request.POST['name'],
            'LastName': request.POST['lastname'],
            'Phone': request.POST['phone'],
            'Email': request.POST['email'],
            'ProductName': request.POST['prop_name'],
            'BouthDate': request.POST['bouth_date'],
            'Description': request.POST['description'],
            # 'form': c_form,
        }
        # assert False
        return render(request, 'index.html', context={'wor': data})
    
    return render(request, 'index.html', context={'form': c_form})