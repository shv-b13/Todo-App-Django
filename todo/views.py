from django.shortcuts import render
from .models import Todo
from .form import TodoForm
from django.shortcuts import redirect

# Create your views here.


def todo(request):
    return render(request, 'todo/todo1.html', {'todo': Todo.objects.all()})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
        return render(request, 'todo/todo_edit.html', {'todo': todo})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'todo': todo})

