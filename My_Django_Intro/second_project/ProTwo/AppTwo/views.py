from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    user_list = User.objects.order_by('last_name')
    my_dict={"swift":"This is a variable named swift",
             'users':user_list}
    return render(request,"index.html",context=my_dict)

def help(request):
    my_dict={"name":"German"}
    return render(request,"help.html",context=my_dict)

