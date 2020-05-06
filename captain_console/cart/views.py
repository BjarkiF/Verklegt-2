from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import Cart
from items.models import Item


@login_required
def index(request):
    cart = Cart.objects.filter(customer_id=request.user.id).first()
    items = []
    for cart_item in cart.items:
        item = Item.objects.get(id=cart_item)
        items.append(item)
    return render(request, 'cart/index.html', {
        'items': items
    })
