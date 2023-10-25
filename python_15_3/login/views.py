from django.shortcuts import render, redirect
from .forms import LogIN, Register
from .models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    form = Register()
    user = User()
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']
        superuser = form.cleaned_data['superuser']
        if name not in user.objects.name:
            user.name = name
            user.password = password
            user.superuser = superuser
            user.save()

    return render(request, 'holder.html', {'form': form})

def login(request):
    form = LogIN(request.POST)
    # user = User()
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']
        v = User.objects.get(name=name)
        if v is not None:
            print('Not none!')
            if v.password == password:
                print(v)
                return redirect('greet', id=v.id)

    return render(request, 'holder.html', {'form': form})

def greet(request, id):
    user = User.objects.get(id=id)
    return render(request, 'greet.html', {'name': user.name, 'superuser': user.superuser})