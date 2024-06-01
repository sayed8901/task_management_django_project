from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_data = forms.TaskForm(request.POST)

        if task_data.is_valid():
            task_data.save(commit=True)
            print(task_data.cleaned_data)
            return redirect('homepage')
        
    else:
        task_data = forms.TaskForm
    
    return render(request, 'add_task.html', {'form': task_data})



def edit_task(request, id):
    target_task = models.Task.objects.get(pk=id)
    print(target_task)

    task_form = forms.TaskForm(instance=target_task)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=target_task)

        if task_form.is_valid():
            task_form.save(commit=True)
            print(task_form.cleaned_data)

            return redirect('homepage')
    
    return render(request, 'add_task.html', {'form': task_form})



def delete_task(request, id):
    target_task = models.Task.objects.get(pk=id)
    target_task.delete()
    print(target_task)

    return redirect('homepage')
