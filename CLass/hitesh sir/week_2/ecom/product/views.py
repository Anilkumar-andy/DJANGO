from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm



# Create your views here.
def home(request):
    #return HttpResponse('<h1>Hello world<h1>')
    
    p=Product.objects.all()#select * from Product
    context={
        'products':p
    }
    return render(request,"product/home.html",context)

def add_product(request):
    context={
        'form': ProductForm
    }
    return render(request,"product/add_product.html",context)
def about_us(request):
    return render(request, "product/about_us.html")