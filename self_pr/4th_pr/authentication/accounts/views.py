from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages     # predifended meesaages from django
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():     #checking wether user exists(returns boolean value[I.e T/F]) or not 
            messages.error(request, "Username does not exist.Invalid username")
            return redirect('_login')
        
        user = authenticate(username=username,password=password) #itreturns an object. for current username
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/accounts/login/')
        else:
            login(request,user) 
            #this is predefined function. make sure other function are not named as login as it may cause recursive function.
            #query_set = User.objects.get(username=username)
            #return render(request, 'accounts/user.html',{'user': query_set})
            # we don't need to use the query User.objects.get(username=username) to retrieve the user object because you already have the authenticated user object obtained from the authenticate() function.
            # The authenticate() function performs both username and password validation and returns the user object if the credentials are valid. So, by the time you reach the else block in your login view, you already have the authenticated user object stored in the user variable.
            #instead we can use
            return render(request, 'accounts/user.html',{'user': user})
    return render(request, 'accounts/login.html')

def logout_page(request):
    messages.info(request, "logout was successful")
    logout(request)
    return redirect('_login')


def register_page(request):
    context={}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user =User.objects.filter(username=username)        #checking from database wether user exists or not
        if user.exists():
            context['info'] = 'alert-danger'
            messages.info(request, " username already exist. Account not created")      #to flash messesage for info that username already exists
            return redirect('_register')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,  
            username = username,
            # password = password         #this will not encrypt the password it will just save the password as string
        )
        user.set_password(password)     #for encrytion purpose
        user.save()
        context['info'] = 'alert-success'
        messages.info(request, " account created Successfully")      #to flash messesage for info that account is created
    return render(request, 'accounts/register.html',context)