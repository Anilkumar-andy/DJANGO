from django.http import HttpResponse
from django.shortcuts import render

'''def home(request):
    #return HttpResponse("Hello world")
    #return render(request,'index.html',{'name':'Anil'})
    content={'name':'hritika'}
    return render(request,'index.html',content)'''

def home(request):
    return render(request,'index.html')
def about_us(request):
    return render(request, "about_us.html")