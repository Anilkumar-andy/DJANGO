from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterCustomer,RegisterSupplier
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'account/login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            user = authenticate(request,username=username,password=password)
            print(type(user))
            if user:
                login(request, user)
                return redirect('index')
            return redirect('login')
        else:
            return render(request,'account/login.html',{'form':form})


# def login_user(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request,'account/login.html',{'form':form})

#     elif request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form['username'].value()
#             password = form['password'].value()
#             user = authenticate(request,username=username,password=password)
#             print(type(user))
#             if user:
#                 login(request, user)
#                 return redirect('index')
#             return redirect('login')
#         else:
#             return render(request,'account/login.html',{'form':form})
def register_user(request):
    return render(request,'account/register.html')
    
    
def logout_user(request):
    logout(request)
    return redirect('login')

def register_supplier(request):
    if request.method == 'GET':
        context={
            'form':RegisterSupplier()
        }
        return render(request,'account/register.html',context)
    elif request.method == 'POST':
        form = RegisterSupplier(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context={
                'form':RegisterSupplier(request.POST)
            }
        return render(request,'account/register.html',context)

        
def register_customer(request):
    if request.method == 'GET':
        context={
            'form':RegisterCustomer()        
        }
        return render(request,'account/register.html',context)
    elif request.method == 'POST':
        pass
    