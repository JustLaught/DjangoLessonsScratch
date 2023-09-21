from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request, aftertext=""):
    return render(request, "company/index.html")

def news(request, aftertext=""):
    return render(request, 'company/news.html')

def managment(request, aftertext=""):
    return render(request, "company/managment.html")

def about(request, aftertext=""):
    return render(request, "company/about.html")

def contacts(request, aftertext=""):
    return render(request, "company/contacts.html")

def branches(request, name=""):
    if name == "london":
        return render(request, "company/branches/london.html")
    elif name == "paris":
        return render(request, "company/branches/paris.html")
    else:
        return render(request, "company/branches.html")