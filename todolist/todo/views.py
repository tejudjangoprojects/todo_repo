from django.shortcuts import render
from todo.models import Todo
from todo.forms import TodoForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
#from django.contrib.auth.decorators import permission_required


# Create your views here.
class TodoListView(ListView):
    model=Todo
class TodoDetailView(DetailView):
    model=Todo
class TodoCreateView(CreateView):
    model=Todo
    fields='__all__'
class TodoUpdateView(UpdateView):
    model=Todo
    fields=('title','date_of_the_task','start_time_of_task','end_time_of_task','status')
class TodoDeleteView(DeleteView):
    model=Todo
    success_url=reverse_lazy('home')
