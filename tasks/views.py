from django.shortcuts import render, get_object_or_404, redirect

from .models import Task

from .forms import TaskForm

from django.contrib import messages

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task/list.html', {'tasks':tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task/task.html', {'task':task})


def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Tarefa cadastrada com sucesso')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'task/addTask.html', {'form':form})


def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if (form.is_valid()):
            task.save()
            messages.info(request, 'Tarefa atualizada com sucesso')
            return redirect('/')
        else:
            return render(request, 'task/editTask.html', {'form':form, 'task':task})    
    else:
        return render(request, 'task/editTask.html', {'form':form, 'task':task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Tarefa deletado com sucesso')
    return redirect('/')