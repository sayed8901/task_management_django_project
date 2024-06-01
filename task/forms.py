from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'

        widgets = {
            'task_assign_date' : forms.DateInput(attrs={'type': 'date'}),
            'task_description' : forms.Textarea(attrs={'type': 'textarea', 'rows': 4}),
            'is_completed': forms.CheckboxInput(attrs={'disabled': 'disabled'}),
        }
        
