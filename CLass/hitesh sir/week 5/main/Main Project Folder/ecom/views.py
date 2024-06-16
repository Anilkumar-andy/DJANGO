from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    # return HttpResponse("Hello world")
    # content={'name':'ItVedant'}
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def contact_us(request):
    return render(request,'contact_us.html')

from .forms import RegisterForm
def register(request):
    context ={
        'form':RegisterForm
    }
    return render(request,'forms_re.html',context)
