from django.shortcuts import render
from basic_app import forms
# Create your views here.

def index(request):
    my_dict = {}
    return render(request, 'basic_app/index.html', context=my_dict)

def forms_page(request):
    form = forms.FormName()
    my_dict = {'form':form}
    return render(request, 'basic_app/forms.html', context=my_dict)