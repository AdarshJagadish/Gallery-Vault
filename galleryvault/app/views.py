from django.shortcuts import render,redirect
from .models import *

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        users=user.objects.all()
        for i in users:
            if email==i.email and password==i.password:
                request.session['login']=i.pk
                return redirect(home)
            else:
                return redirect(login)
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
    if 'login' in request.session:
        users=user.objects.all()
        print(users)
        return render(request,'home.html',{user:users})
    else:
        return redirect(login)
        

# Create your views here.