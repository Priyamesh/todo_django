from django.shortcuts import render
from django.http import HttpResponse   
from django.views.generic.list import ListView

from base.models import Task 
from .models import Task


# Create your views here.

class TaskList(ListView):
    model=Task
    context_object_name='tasks'

