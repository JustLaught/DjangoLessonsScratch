from django.shortcuts import render
import json
import requests

# Create your views here.

def index(request):  
    data = requests.get('https://restcountries.com/v3.1/all').json()
    countries = []
    for e in data:
        countries.append(e['name']['common'])
    return render(request, 'index2.html', {'data': countries})

def country(request, name):
    data = requests.get(f'https://restcountries.com/v3.1/name/{name.lower()}').json()
    return render(request, 'country.html', {'data': data[0]})

def get_region(request):
    data = requests.get('https://restcountries.com/v3.1/all').json()
    regions = set()
    for e in data:
        regions.add(e['region'])

    return render(request, 'regions.html', {'data': regions})

def region(request, region):
    data = requests.get(f'https://restcountries.com/v3.1/region/{region}')
    return render(request, 'region.html', {'data': data})

def get_capital(request, capital):
    data = requests.post(f'https://countriesnow.space/api/v0.1/countries/population/cities', {'city': capital}).json()
    return render(request, 'capital.html', {'data': data})

def get_lang(request, lang):
    data = requests.get(f'https://restcountries.com/v3.1/lang/{lang}').json()
    country = []
    for e in data:
        country.append(e['name']['common']) 
    print(country)
    return render(request, 'index2.html', {'data': country})

def languages(request):
    data = requests.get('https://restcountries.com/v3.1/all').json()
    languages = set()
    for e in data:
        for k, v in e.get('languages', {}).items():
            languages.add(v)

    return render(request, 'languages.html', {'data': languages})

def countries_by_lang(request, lang):
    data = requests.get(f'https://restcountries.com/v3.1/lang/{lang}').json()
    country = []
    for e in data:
        country.append(e['name']['common']) 
    return render(request, 'index2.html', {'data': country})