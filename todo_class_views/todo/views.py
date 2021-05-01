from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import *

# - - - - - - - - - - - - - - - - - - LOGIN-REGISTER- - - - - - - - - - - - - - - - - -  

class UserRegister(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('main_page')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)


class UserLogin(LoginView):
    template_name = "todo/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main_page')


# - - - - - - - - - - - - - - - - - TASK CRUD OPERATIONS - - - - - - - - - - - - - - - - - - 

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/main.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = "task"
    template_name = "todo/task_detail.html"
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'complete']
    success_url = reverse_lazy('main_page')
    #otomatik olarak form adında object veriyor html tarafında

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'complete']
    success_url = reverse_lazy('main_page')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)    
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('main_page')
    template_name = 'todo/task_delete.html'
    
    

    
    
