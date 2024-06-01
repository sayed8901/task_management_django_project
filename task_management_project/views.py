from django.shortcuts import render
from task import models

# Create your views here.
def home(request):
    data = models.Task.objects.all()
    return render(request, 'home.html', context={'data': data})

