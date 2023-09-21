from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def index(request, lang=''):
    context = {
        '': 'Hello World!',
        'sp': 'Holla world!',
        'de': 'Hallo welt!',
        'fr': 'Bonjour world!'
    }
  
    text = {'text': context[lang],}
    return render(request, 'notindex.html', context=text)

def keke(request, text=''):
    temp = {
        '': 'Main page!',
        'football': 'football',
        'basketball': 'basketball',
        'baseball': 'baseball',
        'hockey': 'hockey', 
    }
    context = {
        'text': temp[text],
    }
    return render(request, 'notindex.html', context)

def time(request):
    now = timezone.localtime()

    if 0 <= now.hour <= 9:
        greeting="Good morning"
    elif 9 < now.hour <= 15:
        greeting="Good afternoon"
    elif 15 < now.hour <= 23:
        greeting="Good evening"

    context = {
        'text': now,
        'greeting': greeting,
    }
    return render(request, 'notindex.html', context)