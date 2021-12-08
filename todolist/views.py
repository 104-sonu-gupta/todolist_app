from django.contrib import messages
from django.core import paginator
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from todolist.models import TaskList
from todolist.forms import Taskform
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            print(request.user)
            instance.save()

            messages.success(request, "New task '{}' created successfully.".format(form.data['task']))
        return redirect('todolist')

    else:
        queryset = TaskList.objects.filter(user=request.user)
        paginator = Paginator(queryset, 5)
        page = request.GET.get('pg')
        queryset = paginator.get_page(page)
        content = {
        
            'title' : 'Todolist',
            'tasks' : queryset
        }
        return render(request, 'todolist.html', content)


def index(request):
    return render(request, 'index.html')

@login_required
def contact(request):
    
    content = {
        'title' : 'Contact Us'
    }
    return render(request, 'contact.html', content)


def about(request):

    content = {
        'title' : 'About Us'
    }
    return render(request, 'about.html', content)


@login_required
def delete(request, id):
    queryset = TaskList.objects.get(pk=id)
    if queryset:
        if request.user == queryset.user:
            queryset.delete()
            messages.error(request, "Task deleted successfully.!")
        else:
            messages.error(request, "Access restricted, You are not allowed to delete this task !")
    
    return redirect('todolist')


@login_required
def completed(request, id):
    queryset = TaskList.objects.get(pk=id)
    if request.user == queryset.user:
        queryset.done = not queryset.done
        queryset.save()
    else:
        messages.error(request, "Access restricted, You are not allowed to mark this task !")
    return redirect('todolist')

@login_required
def edit_task(request, id):
    if request.method == "POST":
        queryset = TaskList.objects.get(pk=id)
        form = Taskform(request.POST or None, instance = queryset)    
        # instance needed so that django will know we are updating previous task
        if form.is_valid():
            form.save()
        
        messages.success(request, "Task updated successfully.")
        return redirect('todolist')
    else:
        queryset = TaskList.objects.get(pk = id)
        content = {
            'title' : 'Edit Task',
            'task_obj' : (queryset),
        }
        return render(request, 'edit.html', content)
