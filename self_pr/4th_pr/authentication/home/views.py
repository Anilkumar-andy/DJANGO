from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home/index.html')

@login_required     #to make login compulsory for accessing a url or page
# @login_required(login_url="/accounts/register")       #used to have custom url which can be something else rather than login url
def account_list(request):
    Query=User.objects.all()
    print(Query)
    Context={'ac':Query}
    if request.GET.get('search_ac'):
        print(request.GET.get('search_ac'))
        Query=User.objects.filter(username__icontains=request.GET.get('search_ac'))
    else:
        query = User.objects.all()
    Context={'ac':Query} 
    return render(request,'home/list_account.html',Context)