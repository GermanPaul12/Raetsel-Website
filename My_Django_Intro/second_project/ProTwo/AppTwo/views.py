from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={"swift":"This is a variable named swift",}
    return render(request,"index.html",context=my_dict)

def help(request):
    my_dict={"name":"German"}
    return render(request,"help.html",context=my_dict)

