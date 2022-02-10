from django.shortcuts import render, redirect
import datetime
from .models import Task
from .forms import TodoForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    task_list = Task.objects.filter(done_field=False)
    return render(request, 'to_do_app/index.html', {'task_list': task_list})


def add(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        done_field = request.POST.get('done_field', False)
        task = Task(name=name, description=description, priority=priority, date=date, done_field=done_field)
        task.save()
        return redirect('/to_do_app')
    return render(request, 'to_do_app/add.html')


# def delete(request, task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method == "POST":
#         task.delete()
#         return redirect('/')
#     return render(request, 'to_do_app/delete.html', {'task': task})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('/to_do_app/')



def done_true(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.done_field = True
        task.save()
        return redirect('/to_do_app/')
    # return render(request, 'to_do_app/done_true.html', {'task': task})


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/to_to_app/')
    return render(request, 'to_do_app/edit.html', {'form': form, 'task': task})


def done_tasks(request):
    task_list = Task.objects.filter(done_field=True)
    return render(request, 'to_do_app/done_tasks.html', {'task_list': task_list})


def reopen(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "POST":
        task.done_field = False
        task.save()
        return redirect('/to_do_app/')



