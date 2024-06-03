from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == "POST":
        data=request.POST
        name =data.get('name')
        color=request.POST.get('color')
        drive_type=data.get('drive_type')
        desc=request.POST.get('desc')
        image=request.FILES.get('image')#for file type
        print(data)
        print(name)
        print(color)
        print(drive_type)
        print(desc)
        Cars.objects.create(name=name,color=color,drive_type=drive_type,desc=desc,image=image)   
        return redirect("/")
    return render(request,"home/index.html",context={'page':'Home'})

def carlist(request):
    queryset=Cars.objects.all()#this will give list of dectionary
    print(queryset)
    if request.GET.get('search'):
        print(request.GET.get('search'))
        querset=queryset.filter(name__icontains=request.GET.get('search'))
    return render(request, "home/carlist.html",context={'page':'car list','cars_data':queryset})
    

def update(request,id):  # sourcery skip: extract-method
    queryset=Cars.objects.get(id=id)
    
    if request.method=="GET":
        context={'car':queryset}
        return render(request,'home/update.html',context)
    
    elif request.method=="POST":
        data=list(request.POST.items())#storing all the data in data which is beingto be updated
        print(data)#printing the data in terminal which will be uploaded
        queryset.name=request.POST.get('name')
        queryset.color=request.POST.get('color')
        queryset.drive_type=request.POST.get('drive_type')
        queryset.desc=request.POST.get('desc')
        image=request.FILES.get('image')
        if image:
            queryset.image=image
        queryset.save()
        return redirect("_carlist")
    


    
def delete(request,id):
    print(id)
    queryset=Cars.objects.get(id=id)
    print(queryset)
    queryset.delete()
    return redirect('_carlist')

    