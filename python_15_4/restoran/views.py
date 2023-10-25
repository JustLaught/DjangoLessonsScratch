from django.shortcuts import render, redirect
from .forms import RestRegForm
from .models import Restoran

# Create your views here.


def index(request):
    return render(request, 'index.html')

def addrestoran(request):
    form = RestRegForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        restoran = Restoran(name=form.cleaned_data['name'],
                            spec=form.cleaned_data['spec'],
                            address=form.cleaned_data['address'],
                            web_site=form.cleaned_data['web_site'],
                            phone=form.cleaned_data['phone'])
        restoran.save()
        return redirect('index')
    return render(request, 'adding.html', {'form': form})

def showrestorans(request, spec='all'):
    if spec == 'all':
        restorans = Restoran.objects.all()
    else:
        restorans = Restoran.objects.filter(spec__contains=spec)
    return render(request, 'showing.html', {'data': restorans})

def showrestoran(request, id):
    restoran = Restoran.objects.get(id=id)
    form = RestRegForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['delete']:
            restoran.delete()
            restoran.save()
            return redirect('showrestorans')
        restoran.name = form.cleaned_data['name']
        restoran.spec = form.cleaned_data['spec']
        restoran.address = form.cleaned_data['address']
        restoran.web_site = form.cleaned_data['web_site']
        restoran.phone = form.cleaned_data['phone']
        restoran.save()
        return redirect('showrestorans')

    return render(request, 'showone.html', {'data': restoran, 'form': form})