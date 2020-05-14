from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart
from items.models import Item
from users.models import User, UserCountry, UserCard
from users.forms.forms import EditAddressForm, UserCardForm
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
    cart = Cart.objects.filter(user_id=request.user.id).first()
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
def checkout(request): # TODO: klára
    if request.method == 'POST':
        address_form = EditAddressForm(data=request.POST)
        card_form = UserCardForm(data=request.POST)
        if address_form.is_valid() and card_form.is_valid():
            card = UserCard.objects.create(
                name=request.POST['name'],
                number=request.POST['number'],
                exp_month=request.POST['exp_month'],
                exp_year=request.POST['exp_year'],
                cvc=request.POST['cvc']
            )
            context = {
                'cart': Cart.objects.get(user_id=request.user.id),
                'address': get_address_dict(address_form),
                'card': card
            }
        elif card_form.is_valid():
            pass
        return render(request, 'cart/review.html', context)
    context = {
        'user': User.objects.get(id=request.user.id),
        'address_form': EditAddressForm(),
        'card_form': UserCardForm(),
    }
    return render(request ,'cart/checkout.html', context)

def get_address_dict(form):
    country = UserCountry.objects.get(id=form.country_id)
    dict = {
        'street': form.street_name + ' ' + form.house_num,
        'city': form.zipcode + ' ' + form.city,
        'country': country.country_name
    }
    return dict