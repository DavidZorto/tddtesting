from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    tasks= Task.objects.all()
    return render(request, 'task/index.html', {'tasks': tasks})

def detail(request, pk):
    tasks=Task.objects.get(pk=pk)
    return render(request, 'task/deatil.html',{'tasks': tasks})