from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def cart(request):
    return render(request, "cart/cart.html")
def payment(request):
    return render(request, "cart/payment.html")