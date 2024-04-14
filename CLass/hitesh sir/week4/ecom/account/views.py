from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View

# Create your views here.
#class based views
class Login_View(View):
    def get(self,request):
        form =LoginForm()
        return render(request, "account/login.html",{'form':form})
    def post(self,request):
        form =LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].value()
            password=form['password'].value()
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('-index')
            return redirect('-login')
        else:
            return render(request,'account/login.html',{'form':form})
    


#function based views
'''def login_user(request):
    if request.method =='GET':
        form =LoginForm()
        return render(request, "account/login.html",{'form':form})
    elif request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].value()
            password=form['password'].value()
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('-index')
            return redirect('-login')
        else:
            return render(request,'account/login.html',{'form':form})'''
def register(request):
    return render(request,"account/register.html")
def logout_user(request):
    logout(request)
    return redirect('-index')
