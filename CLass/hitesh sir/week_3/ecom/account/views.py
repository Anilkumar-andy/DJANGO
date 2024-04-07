from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, "account/login.html")
def register(request):
    return render(request,"account/register.html")
def logout(request):
    return redirect('-index')
