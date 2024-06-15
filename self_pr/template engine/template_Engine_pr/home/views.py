from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[
        {'name':'Anil','age':24},
        {'name':'Omi','age':22},
        {'name':'Salim','age':21},
    ]
    text="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi molestiae sequi earum neque obcaecati, reiciendis quo, enim quos perferendis esse fugiat, ab id eius consequuntur incidunt sunt voluptates autem molestias harum alias est velit exercitationem provident? Animi blanditiis culpa explicabo id excepturi eum praesentium quis dolor cupiditate optio quae consequatur totam, nemo laborum maxime repellendus ipsa, ad aspernatur esse numquam. Nostrum totam, et sed eos quia amet, consectetur illum commodi, architecto saepe itaque odit vel harum quo consequatur. Dolorem, sequi minus! Inventore, labore nihil perspiciatis sequi porro atque veritatis harum necessitatibus perferendis numquam commodi vitae? Et veniam cum excepturi ex!"""
    
    vechile=['zx10r','h2r','v4s','r1','supra']
    
    empty=[]
    
    return render(request,'home/index.html',context={'page':'home page','variable_name':peoples,'text':text,'vechiles':vechile , 'empty_list' : empty})

def about(request):
     return render(request,'home/about.html',context={'page':'about page'})
 
def contact(request):
     return render(request,'home/contact.html',context={'page':'contact page'})
    