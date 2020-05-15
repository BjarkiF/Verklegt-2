from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, Order
from items.models import Item
from users.models import User, UserCard, UserAddress
from users.forms.forms import CheckoutAddressForm, UserCardForm
import datetime

@login_required
def index(request):
    cart = Cart.objects.filter(user_id=request.user.id).first()
    items, total = get_cart_items(cart)
    return render(request, 'cart/index.html', {
        'items': items,
        'total': total,
    })


@login_required
def add_to_cart(request, id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user_id=request.user.id).first()
        if not cart:
            cart = Cart.objects.create(user_id=request.user.id, items=[])
        if not cart.items:
            cart.items = []
        cart.items.append(id)
        cart.save()
        return redirect('/cart/')
    else:
        return redirect('/users/')


@login_required
def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, user_id=request.user.id)
    cart.items.remove(str(id))
    cart.save()
    return redirect('/cart/')


@login_required
def remove_from_cart_all(request, id):
    cart = Cart.objects.get(user_id=request.user.id)
    items = cart.items
    items[:] = (value for value in items if value != str(id))
    cart.items = items
    cart.save()
    return redirect('/cart/')


@login_required
def checkout(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user_id=request.user.id)
        items, total = get_cart_items(cart)
        address_form = CheckoutAddressForm(data=request.POST)
        card_form = UserCardForm(data=request.POST)
        if card_form.is_valid():
            numstring = request.POST['number']
            card_name = request.POST['name']
            card = 'xxxxxxxxxxxx' + numstring[-4:]
            if request.POST['address-radio']=='new_address':
                if address_form.is_valid() and request.POST['country_id']: # TODO: lmao validata betur
                    address_new = UserAddress.objects.create(
                        user_id=request.user.id,
                        street_name=request.POST['street_name'],
                        house_num=request.POST['house_num'],
                        zipcode=request.POST['zipcode'],
                        city=request.POST['city'],
                        country_id=request.POST['country_id'],
                    )
                    request.session['checkout_address'] = address_new.id
                    context = {
                        'address': address_new,
                        'card': card,
                        'card_name': card_name,
                        'items': items,
                        'total': total,
                    }
                else:
                    return redirect('/cart/checkout')
            else:
                address_temp = UserAddress.objects.filter(user_id=request.user.id).first()
                request.session['checkout_address'] = address_temp.id
                context = {
                    'address': address_temp,
                    'card': card,
                    'card_name': card_name,
                    'items': items,
                    'total': total,
                }
            return render(request, 'cart/review.html', context)
    context = {
        'user': User.objects.get(id=request.user.id),
        'address_form': CheckoutAddressForm(),
        'card_form': UserCardForm(),
    }
    return render(request, 'cart/checkout.html', context)

def review(request):
    return render(request,'cart/review.html')

def confirm(request):
    cart = Cart.objects.get(user_id=request.user.id)
    checkout_items, checkout_total = get_cart_items(cart)
    checkout_item_ids = []
    for item in checkout_items:
        checkout_item_ids.append(item[0].id)
    address = request.session.get('checkout_address')
    Order.objects.create(
        user_id=request.user.id,
        address_id=address,
        items=checkout_item_ids,
        total=checkout_total,
        date=datetime.datetime.now()
    )
    cart.items = []
    cart.save()
    return render(request, 'cart/confirm.html')

def get_cart_items(cart):
    total = 0
    found = 0
    if cart:
        items = []
        for cart_item in cart.items:
            item = Item.objects.get(id=cart_item)
            for list in items:
                if item == list[0]:
                    list[1] += 1
                    found = 1
            if not found:
                items.append([item, 1])
            total += item.price
            found = 0
    else:
        items = []
    return items, total
