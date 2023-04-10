from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User 
from . forms import TaskForm
from .  models import Task

import datetime

# today=datetime.date.today().strftime("%Y-%m-%d")
today=datetime.date.today()
date=''

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            date=request.POST.get('date')
            if request.POST.get('date')=='':
                date=today
            if request.POST.get('task')=='' :
                messages.error(request, "Task cannot be empty")
            else:
                task=Task.objects.create(
                
                task=request.POST.get('task'),
                user=request.user,
                created=date
            )
                task.save()
            print(request.POST.get('date'))
        tasks=request.user.task_set.all().filter(created=today)
        context={'tasks':tasks}

        return render(request, 'home.html',context)
    return redirect('login')

def ByDate(request):
    if request.method == 'POST':
        date= request.POST.get("date")
        tasks=request.user.task_set.all().filter(created=date)
        context={'tasks':tasks}

        return render(request, 'home.html',context)

def Register(request):
    form=UserCreationForm()
    page='register'
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    context={'form':form,'page':page}
    return render(request, 'main.html',context)

def Log(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "User doesnot exist")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'main.html')

def LogOut(request):
    logout(request)
    return redirect('login')




def Delete(request,pk):
    task= Task.objects.get(id=pk)
    task.delete()
    return redirect('home')


def Edit(request,pk):
  
    tak=Task.objects.get(id=pk) #this simply returns task model attributes and value as dictionary
    form=TaskForm(instance=tak)
    if request.method == "POST":
            tak.task=request.POST.get('task')
            tak.save()
            return redirect('home')
    context={'form':form,'act':'edit'}
    return render(request,'edit.html',context)
