from django.shortcuts import render, HttpResponse
import json
import random 
from .models import Writing


# Create your views here.
def index(request):
    lst = ['Молись Богу, але греби до берега.', 'Незабаром ви станете свідками дива.', 'Ви людина з гарним почуттям справедливості, настав ваш час.', 'Метафора може врятувати вам життя.', 'Усі твої печалі зникнуть.']
    res = random.choice(lst)
    print(res)
    # return HttpResponse(json.dumps({'predict': str(res)})) Not showing STR()
    return HttpResponse(f'Predict: {res}')

def randomnumber(request):
    if request.GET['a'] or ['b'] is None:
        number = random.randint(-300, 300)

    elif request.GET['a'] == 'lst':
        number = [random.randint(-300, 300),random.randint(-300, 300),random.randint(-300, 300),random.randint(-300, 300)]

    else: number = random.randint(int(request.GET['a']), int(request.GET['b']))

    return HttpResponse(json.dumps({'RandomNumber': number}))

def writing(request):
    writ = Writing.objects.all()
    writerW = []
    typeW = []
    textW = []
    for i in writ:
        writerW.append(i.writer.name)
        typeW.append(i.type)
        textW.append(i.writing)
    # res = {
    #     'Author': writer,
    #     'Type': type,
    #     'Text': text
    # }
    if request.GET['type'] in typeW:
        w = Writing.objects.get(type=request.GET['type'])
        text = []
        for i in w:
            text.append(i.writing)
        return HttpResponse(json.dumps({'Text': random.choice(text)}))
    elif request.GET['author'] in writerW:
        w = Writing.objects.get(writer=request.GET['author'])
        text = []
        for i in w:
            text.append(i.writing)
        return HttpResponse(json.dumps({'Text': random.choice(text)}))

    else: return HttpResponse(json.dumps({'Text': random.choice(textW)}))