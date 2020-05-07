from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart
from items.models import Item
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
    cart = Cart.objects.filter(user_id=request.user.id).first()
    if cart:
        items = []
        for cart_item in cart.items:
            item = Item.objects.get(id=cart_item)
            items.append(item)
    else:
        items = []
    #     try:
    #         Users.objects.get(user_id=request.user.id)
    #     except ObjectDoesNotExist:
    #         user_temp = Users.objects.create(user_id=request.user.id)
    #         user_temp.save()
    #     Cart.objects.create(user_id=request.user.id, items=[])
    #     items = []
    return render(request, 'cart/index.html', {
        'items': items
    })



def add_to_cart(request, id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id=request.user.id).first()
        if not cart:
            cart = Cart.objects.create(user_id=request.user.id)
        if not cart.items:
            cart.items = []
        cart.items.append(id)
        cart.save()
        return index(request)
    else:
        return redirect('/users/')

def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, user_id=request.user.id)
    cart.items.remove(str(id))
    cart.save()
    return index(request)
