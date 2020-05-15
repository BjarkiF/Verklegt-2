from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.shortcuts import render, redirect
from users.models import Profile, UserAddress, UserItemSearch
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm, EditAddressForm #, EditCountryForm
from django.contrib.auth.models import User
from cart.models import Order
from cart.views import get_cart_items


def register(request): # TODO: notandi fær ekki villu ef eitthvað klikkar
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    return render(request, 'users/register.html', {
        'form': RegisterForm()
    })


def recover(request):
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save()
            #return redirect('RecoverSen')
            return render(request, 'users/mail_sent.html')
    return render(request, 'users/recover.html', {
        'form': UserCreationForm()
    })


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form_user = EditUserForm(data=request.POST)
        form_extended = EditProfileForm(data=request.POST)
        if form_user.is_valid() and form_extended.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            if request.POST['img']:
                profile.img = request.POST['img']
            if request.POST['phone']:
                profile.phone = request.POST['phone']
            profile.save()
            return redirect('Profile')
    return render(request, 'users/edit_profile.html', {
        'form_user': EditUserForm(instance=user),
        'form_extended': EditProfileForm(instance=profile)
    })


@login_required
def profile(request):
    return render(request, 'users/profile.html', {
        'user': User.objects.filter(id=request.user.id).first(),
        'profile': Profile.objects.filter(user_id=request.user.id).first(),
        'address': UserAddress.objects.filter(user_id=request.user.id).first(),
    })


@login_required
def edit_address(request):
    address = UserAddress.objects.filter(user_id=request.user.id).first()
    if request.method == 'POST':
        form = EditAddressForm(data=request.POST)
        if form.is_valid():
            address.street_name = request.POST['street_name']
            address.house_num = request.POST['house_num']
            address.city = request.POST['city']
            address.zipcode = request.POST['zipcode']
            address.country_id = request.POST['country_id']
            address.save()
            return redirect('Profile')
    return render(request, 'users/edit_address.html', {
        'form': EditAddressForm(instance=address),
        #'country_select': UserCountry.objects.all()
    })


@login_required
def get_search_history(request):
    context = {
        'all_searches': UserItemSearch.objects.filter(user_id=request.user.id)
    }
    return render(request, 'users/search_history.html', context)


@login_required
def get_order_history(request):
    context = {
    'all_orders':  Order.objects.filter(user_id=request.user.id)
    }
    return render(request, 'users/order_history.html', context)

@login_required
def order_details(request, id):
    order = Order.objects.get(id=id)
    context = {
    'order': order,
    'items': get_cart_items(order)[0],
    'address': UserAddress.objects.get(id=order.address_id),
    }
    return render(request, 'users/order_details.html', context)