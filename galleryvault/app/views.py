from django.shortcuts import render,redirect
from .models import *

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(name,username,email,password)
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(username,email,password)
        data=user.objects.create(username=username,email=email,password=password)
        data.save
        return redirect(login)
    return render(request,'register.html')

def home(request):
    return render(request,'home.html')

# Create your views here.
