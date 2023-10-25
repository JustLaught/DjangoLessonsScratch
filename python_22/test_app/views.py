from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse('TEST APP!')

class IndexView(View):
    def get(self, request):
        return HttpResponse('TEST CLASS VIEW!!')
    
    # def post(self, request):
    #     return HttpResponse('TEST CLASS VIEW!!')

class TaskView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'

class AddTaskView(CreateView):
    model = Task
    template_name = 'create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('index')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(action=form.cleaned_data['action'],
                            deadline=form.cleaned_data['deadline'],
                            responsible=form.cleaned_data['responsible']
                            )
            new_task.save()
            return redirect('index')
        return render(request, 'create_task.html', {'form': form})
    else:       
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})
    
class AddTaskView2(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task(action=form.cleaned_data['action'],
                            deadline=form.cleaned_data['deadline'],
                            responsible=form.cleaned_data['responsible']
                            )
            new_task.save()
            return redirect('index')
        return render(request, 'create_task.html', {'form': form})