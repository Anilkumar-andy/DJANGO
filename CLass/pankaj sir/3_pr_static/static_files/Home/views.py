from django.shortcuts import render
from django.http import HttpResponse

from django.templatetags.static import static

def f_css(request):
   css_url = static('css/bootstrap.min.css')
   # Do something with the CSS URL

def f_html(request):
   img_url = static('img/')

def firstpage(request):
   return render(request,"index.html")

'''
def first(request):

   return HttpResponse("hello andy")
   '''