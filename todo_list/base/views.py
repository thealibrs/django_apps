from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView# form yaratır
from django.urls import reverse_lazy
from .models import Task


# Create your views here.
class TaskList(ListView):
    #generates task.html
    model = Task
    # html kısmında objeyi hangi isimle gödereceğini belirliyor
    context_object_name = "tasks"
    
class TaskDetail(DetailView):
    # eğer kendin tanımlamazsa
    # otomatik olarak generates task_detail.html
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasks')
    