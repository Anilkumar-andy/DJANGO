from django.shortcuts import render

from .forms import EmployeeForm
from .models import UserProfile

# Create your views here.
def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html',{'form':form})

def employee_list(request):
    employees = UserProfile.objects.all()
    return render(request,'employee_list.html',{'employees':employees})




