from django.shortcuts import render, redirect
from .forms import LogInForm
from .models import User

# Create your views here.

def index(request):
    form = LogInForm(request.POST)
    db = User()
    if form.is_valid():
        if form.cleaned_data['login'] in db.login:
            for dbu in db:
                if form.cleaned_data['login'] == dbu.login and form.cleaned_data['password'] == dbu.password:
                    user = {'name': dbu.name, 'superuser': dbu.superuser}
                    return render(request, 'index.html', context={'user': user})
        else: return redirect('404page.html')

    return render(request, 'index.html', context={'form': form})


def notfoundpage(request):
    return render(request, '404page.html')