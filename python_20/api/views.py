from django.shortcuts import render, HttpResponse
from django.utils import timezone, dateformat
from .service import NumService
from uuid import uuid4
import json
import datetime


# Create your views here.
def test(request):
    # NumService.uppNumber()
    # return HttpResponse(f'number: {json.dumps(NumService.getNumber())}')
    data = {
        'first': 500,
        'second': True
    }
    return HttpResponse(f'{json.dumps(data)}')

def uuid(request):
    id = uuid4()
    return HttpResponse(f'id: {json.dumps({"uuid": str(id)})}')

def timeOnServer(request):
    time = dateformat.format(timezone.now(), 'D Y-m-d H:i:s')
    return HttpResponse(f'Time on server is: {time}')

def greetTime(request):
    now = datetime.datetime.now().hour
    time = dateformat.format(timezone.now(), 'D Y-m-d H:i:s')
    if 5 < now <= 12 :
        greet = 'Good morning'
    elif 12 < now <= 18 :
        greet = 'Good day'
    elif 18 < now <= 23 :
        greet = 'Good evening'
    elif 23 < now <= 5 :
        greet = 'Good night'

    data = {
        'time': now,
        'greet': greet
    }
    return HttpResponse(json.dumps(data))

def multiply(request, a, b):
    result = a * b
    return HttpResponse(json.dumps({'result': result}))

def multiply2(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    result = a * b
    return HttpResponse(json.dumps({'result': result}))

def adding(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a + b
    except:
        pass

    return HttpResponse(json.dumps({'result': result}))

def midle(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = (a + b) // 2
    except:
        result = 'Incorect Input'

    return HttpResponse(json.dumps({'result': result}))

def minimum(request):
    try:
        lst = map(int, request.GET.values())
        result = min(lst)
    except:
        result = 'Incorect Input'

    return HttpResponse(json.dumps({'result': result}))

def maximum(request):
    try:
        lst = map(int, request.GET.values())
        result = max(lst)
    except:
        result = 'Incorect Input'

    return HttpResponse(json.dumps({'result': result}))

def to_power(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
        result = a ** b
    except:
        result = 'Incorect Input'

    return HttpResponse(json.dumps({'result': result}))