from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm



# Create your views here.
def product(request):
    #return HttpResponse('<h1>Hello world<h1>')
    
    p=Product.objects.all()#select * from Product
    context={
        'products':p
    }
    return render(request,"product/product.html",context)

def add_product(request):
    if request.method == 'GET':
        context={
            'form': ProductForm()
        }
        return render(request,"product/add_product.html",context)
    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            print("Product added")
        else:
            return redirect('add-product')
        return redirect('-product')
def show_details(request):
    pass
