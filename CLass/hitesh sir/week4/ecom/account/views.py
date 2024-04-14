from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method =='GET':
        form =LoginForm()
        return render(request, "account/login.html",{'form':form})
    elif request.method == 'POST':
        form =LoginForm(request.POST)
        username=form['username'].Value()
        user = User.objects.get(username=username)
        print(user)
        return redirect('-login')
def register(request):
    return render(request,"account/register.html")
def logout(request):
    return redirect('-index')
