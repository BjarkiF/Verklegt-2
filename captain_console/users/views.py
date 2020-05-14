from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.shortcuts import render, redirect
from users.models import Profile, UserAddress, UserCountry
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm, EditAddressForm #, EditCountryForm
from django.contrib.auth.models import User


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

# TODO: Skoða hvernig þetta er saveað, afhverju virkar ekki form.save?
@login_required
def edit_address(request):
    address = UserAddress.objects.get(user_id=request.user.id)
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

