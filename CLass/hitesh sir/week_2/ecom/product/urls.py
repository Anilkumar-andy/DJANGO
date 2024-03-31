from django.urls import path
from product.views import *

urlpatterns = [
    #path('home/',home,name='home')
    path('',home,name='home'),
    path('add_product/',add_product,name="add-product"),
    path('about_us/',about_us,name="About_us")
]
