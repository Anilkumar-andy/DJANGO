from django.urls import path
from product.views import *

urlpatterns = [
    #path('home/',home,name='home')
    path('',product,name='-product'),
    path('add_product/',add_product,name="add-product"),
    path('details/<int:id>/',show_details)
]
