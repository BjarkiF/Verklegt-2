from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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


def add_to_cart(request, id):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, customer_id= request.user.id)
        if cart.items:
            cart.items.append(id)
        else:
            cart.items = [id]
        cart.save()
        return index(request)
    else:
        return redirect('/users/')

def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, customer_id=request.user.id)
    cart.items.remove(str(id))
    cart.save()
    return index(request)
