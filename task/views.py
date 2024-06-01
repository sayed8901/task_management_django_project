from django.shortcuts import render, redirect
from . import forms

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


