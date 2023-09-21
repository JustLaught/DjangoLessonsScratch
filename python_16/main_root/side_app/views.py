from django.shortcuts import render, redirect
from .forms import AddContact
from .models import PhoneBook

# Create your views here.


def index(request):
    return render(request, 'phone_book/index.html')

def add_phone(request):
    form = AddContact(request.POST)
    if request.method == 'POST' and form.is_valid():
        contact = PhoneBook(
            name = form.cleaned_data['name'],
            lastname = form.cleaned_data['lastname'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone'],
            about = form.cleaned_data['about']
        )
        contact.save()
        return redirect('index')
    
    return render(request, 'phone_book/add_phone.html', context={'form': form})

def show_contact(request):
    data = PhoneBook.objects.all()
    return render(request, 'phone_book/show_contact.html', context={'data': data})

def contact(request, id):      
    form = AddContact(request.POST) 
    if request.method == 'GET':
        contact = PhoneBook.objects.get(id=id)
        data = {
            'name':contact.name, 'lastname':contact.lastname, 'email':contact.email, 'phone':contact.phone, 'about':contact.about
            }
        form = AddContact(data)    

    if request.method == 'POST' and form.is_valid():        
        contact = PhoneBook.objects.get(id=id)
        contact.name = form.cleaned_data['name']
        contact.lastname = form.cleaned_data['lastname']
        contact.email = form.cleaned_data['email']
        contact.phone = form.cleaned_data['phone']
        contact.about = form.cleaned_data['about']
        contact.save()   

    return render(request, 'phone_book/contact.html', {'contact': contact, 'form':form})


def delete_contact(request, id):
    if request.method == "GET":
        contact = PhoneBook.objects.get(id=id)
        contact.delete()

    return redirect('show_contact')


def serch(request):
    if request.method == 'POST':
        data = PhoneBook.objects.filter(name__icontains=request.POST['name_serch']) # for last name ['lastname_serch'] commented in serch.html
        data2 = PhoneBook.objects.filter(lastname__icontains=request.POST['name_serch'])
        data = data.union(data2)
        return render(request, 'phone_book/show_contact.html', {'data': data})
    return render(request, 'phone_book/serch.html')