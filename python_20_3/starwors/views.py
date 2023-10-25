from django.shortcuts import render
import requests

# Create your views here.
API = 'https://swapi.dev/api/'
# films/ ; people/ ; planets/ ; species/ ; vehicles/ ; starships/
def index(request):
    data = requests.get('https://swapi.dev/api/films/').json()
    return render(request, 'home.html', {'data': data['results']})

def film(request, title):
    data = requests.get(f'https://swapi.dev/api/films/').json()
    for i in data['results']:
        if i['title'] == title:
            data = i
    return render(request, 'film.html', {'data': data})

def heros(request):
    data = requests.get(f'https://swapi.dev/api/people/').json()
    return render(request, 'heros.html', {'data': data['results']})

def hero(request, title):
    data = requests.get(f'https://swapi.dev/api/people/').json()
    for i in data['results']:
        if i['name'] == title:
            data = i
    return render(request, 'film.html', {'data': data})

def planets(request):
    data = requests.get(f'https://swapi.dev/api/planets/').json()
    print(data)
    return render(request, 'planets.html', {'data': data['results']})

def planet(request, title):
    data = requests.get(f'https://swapi.dev/api/planets/').json()
    for i in data['results']:
        if i['name'] == title:
            data = i
    return render(request, 'planet.html', {'data': data})

def ships(request):
    data = requests.get(f'https://swapi.dev/api/starships/').json()
    print(data)
    return render(request, 'ships.html', {'data': data['results']})

def ship(request, title):
    data = requests.get(f'https://swapi.dev/api/starships/').json()
    for i in data['results']:
        if i['name'] == title:
            data = i
    return render(request, 'ship.html', {'data': data})