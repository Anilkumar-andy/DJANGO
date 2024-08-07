from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
import os
from .models import Product
from django.views import View

# Create your views here.
# '''
# def home(request):
#     data='ITVEDANT'
    
#     if os.path.exists('product/templates/product/home.html'):
#             file=open('product/templates/product/home.html', 'rb')
#             response = FileResponse(file)
#             response['Content-Disposition'] = 'attachment; filename="your_file_name.html"'
#             return response
#     else:
#         # Handle the case where the file does not exist
#         return HttpResponse("File not found", status=404)
#     # return FileResponse(request,open(''))

# '''
# def home(request):
#     from django.template.loader import render_to_string

#     def generate_html_file():
#         data = {
#         'name': 'Alice',
#         'age': 30,
#         }
#         rendered_html = render_to_string('product/home.html', data)
    
#         return rendered_html
#     from django.http import HttpResponse

    
#     rendered_html = generate_html_file()

#     response = HttpResponse(rendered_html, content_type='text/html')
#     response['Content-Disposition'] = 'attachment; filename="output.html"'

#     return response

def show_product(request):
    # name="ITVedant"
    p=Product.objects.all() #select * from Product
    context = {
        'products':p
    }
    return render(request,"product/products.html",context)


# def add_product(request):
#     if request.method == 'GET':
#         context={
#             'form' : ProductForm()
#         }
#         return render(request,'product/add_product.html',context)
#     elif request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             context={
#                 'form':ProductForm(request.POST)
#             }
#             return render(request,'product/add_product.html',context)

#class based views
class AddProduct(View):
    def get(self,request):
        context={
            'form' : ProductForm()
        }
        return render(request,'product/add_product.html',context)
    def post(self,request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context={
                'form':ProductForm(request.POST)
            }
            return render(request,'product/add_product.html',context)

class UpdateProduct(View):
    def get(self,request,id):
        data = get_object_or_404(Product,id=id)
        # data = Product.objects.get(id=id)
        context={
            'form': ProductForm(instance=data)
        }
        return render(request, 'product/update_product.html',context)
    def post(self,request,id):
        product = get_object_or_404(Product,id=id)
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('about-product',id)
        else:
            context={
                'form':ProductForm(request.POST)
            }
            return render(request,'product/update_product.html',context)

def show_details(request,id):
    p = get_object_or_404(Product,id=id)
    context = {
        'product':p
    }
    return render(request,'product/product_detail.html',context)

def remove_product(request,id):
    p = get_object_or_404(Product,id=id)
    p.delete()
    return redirect('show-product')

