from django.urls import path
from product.views import *

urlpatterns = [
    #path('home/',home,name='home')
    path('',home,name='home'),
]
