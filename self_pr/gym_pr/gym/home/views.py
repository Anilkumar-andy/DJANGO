from django.shortcuts import render

# Create your views here.
def gymhome(request):
    return render(request,'home/index.html')