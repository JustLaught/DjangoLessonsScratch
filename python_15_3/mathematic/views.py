from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    if request.method == 'POST':
        if request.POST['opt'] == 'min':          
            value = min([request.POST['first'], request.POST['second'], request.POST['third']])
        elif request.POST['opt'] == 'max':
            value = max([request.POST['first'], request.POST['second'], request.POST['third']])
        elif request.POST['opt'] == 'sum':
            value = sum([int(request.POST['first']), int(request.POST['second']), int(request.POST['third'])])
        return redirect('output', data=value)
    return render(request, 'index1.html')

def output(request, data):
    return render(request, 'output.html', {'data': data})
