from django.shortcuts import render, redirect
from .models import Reader, Book

# Create your views here.


def index(request):
    return render(request, 'index.html')

def show_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'data': books})

def show_readers(request):
    readers = Reader.objects.all()
    return render(request, 'readers.html', {'data': readers})

def show_onhand(request, id):
    pass