from django.shortcuts import render
from .forms import RewievForm, SiteForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def review(request):
    form = RewievForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return render(request, 'showinfo.html', {'data': form.cleaned_data})
    return render(request, 'registerform.html', {'form': form})

def sitereview(request):
    form = SiteForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return render(request, 'showinfo.html', {'data': form.cleaned_data})
    return render(request, 'registerform.html', {'form': form})