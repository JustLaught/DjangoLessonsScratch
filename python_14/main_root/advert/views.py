from django.shortcuts import render, HttpResponse
from .forms import AdvForm

# Create your views here.

def index(request):
    form = AdvForm(request.POST)
    values = {}
    if form.is_valid():
        values = {
            'name': form['name'],
            'surname': form['surname'],
            'email': form['email'],
            'age': form['age'],
            'gender': form['gender']
        }
    return render(request, 'adv/index.html', {'form':form, 'values': values})