from django.shortcuts import render, HttpResponse
from .forms import UserForm, UsNum

# Create your views here.

def hello(request):
    form = UserForm(request.POST)
    if form.is_valid():
        return HttpResponse(f"Hello {form.cleaned_data['name']} {form.cleaned_data['surname']}")
    return render (request, 'hello_user/index.html', {'form': form})

def simple(request):
    form = UsNum(request.POST)
    if form.is_valid():
        num1 = form.cleaned_data['first']
        num2 = form.cleaned_data['second']
    lst = []

    for x in range(num1, num2+1):
        simple = True
        for j in range(2, x):
                simple = False
                break
        if simple:
            lst.append(x)

    return render(request, 'hello_user/simple.html', {'form':form,'lst':lst})