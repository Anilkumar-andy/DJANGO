from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request,'cart/cart.html')

def payment(request):
    return render(request,'cart/payment.html')