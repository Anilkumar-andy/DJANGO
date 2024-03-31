from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse('<h1>Hello world<h1>')
    data='Andy'
    return render(request,"product/home.html",{'name':data})