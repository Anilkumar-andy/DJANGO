from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CartItem
# Create your views here.

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        #Handle adding item to cart
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        #you need to handle cart managemnt here
        CartItem.objects.create(
            user = request.User,
            product_name = product_name,
            quantity=quantity,
            price=price
        )
    return redirect('shopping_cart:cart_view')

@login_required
def remove_from_cart(request,item_id):
    # Handle removing item from cart
    cart_item= CartItem.objects.get(id= item_id)
    cart_item.delete()
    return redirect('shopping_cart:cart_view')

@login_required
def cart_view(request):
    #retrieve cart items and render cart template
    cart_items= CartItem.objects.filter(user=request.user)
    total_price = sum(item.price *item.quantity for item in cart_items)
    context={
        'cart_items':cart_items,
        'total_price':total_price
    }
    return render(request,'shopping_cart/cart.html', context)
