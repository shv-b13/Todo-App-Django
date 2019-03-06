from django.shortcuts import render
from .models import Todo
# Create your views here.


def todo(request):
    return render(request, 'todo/todo1.html', {'todo': Todo.objects.all()})