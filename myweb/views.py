from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .models import *

# Create your views here.
def index(req):
	if req.method == "POST":
		getname = req.POST.get('name')
		gettext = req.POST.get('text')
		add = comment2(name=getname, text=gettext)
		add.save()
	return render(req, 'myweb/index.html')

def stand(req):
	return render(req, 'myweb/stand.html')

def stand1(req):
	return render(req, 'myweb/stand1.html')

def stand2(req):
	return render(req, 'myweb/stand2.html')

def stand3(req):
	return render(req, 'myweb/stand3.html')

def stand4(req):
	return render(req, 'myweb/stand4.html')

def stone(req):
	return render(req, 'myweb/stone.html')

def stone1(req):
	return render(req, 'myweb/stone1.html')

def stone2(req):
	return render(req, 'myweb/stone2.html')

def stone3(req):
	return render(req, 'myweb/stone3.html')

def stone4(req):
	return render(req, 'myweb/stone4.html')

#def login(req):
#    	return render(req, 'myweb/login.html')

def logout(req):
    return redirect('login')


def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)
