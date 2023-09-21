from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request, aftertext=""):
    return render(request , 'city_map/index.html' )

def news(request, aftertext=""):
    return render( request ,'city_map/news.html')

def vilage_liders(request, aftertext=""):
    return render(request,'city_map/vilage-leaders.html')

def fact_no_cap(request, aftertext=""):
    return render(request,"city_map/fact-no-cap.html")

def emergency_numbers(request, aftertext=""):
    return render(request ,"city_map/emergency-numbers.html" )

def history_site(request, name=""):
    if name == "people":
        return render (request,"city_map/history_f/people.html")
    
    elif name == "photos":
        return render(request,"city_map/history_f/photos.html")
    
    else: return render(request,"city_map/history.html")