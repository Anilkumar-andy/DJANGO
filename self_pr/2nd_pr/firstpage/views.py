from django.shortcuts import render
#self
from django.http import HttpResponse

# Create your views here.
def firstpage(request):
    return render(request,"index.html")