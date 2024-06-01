from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_data = forms.CategoryForm(request.POST)

        if category_data.is_valid():
            category_data.save(commit=True)
            print(category_data.cleaned_data)
            return redirect('homepage')
        
    else:
        category_data = forms.CategoryForm
    
    return render(request, 'add_category.html', {'form': category_data})