from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request, 'users/register.html', {
        'form': RegisterForm()
    })

@login_required
def edit_profile(request):
    profile = Profile.objects.filter(user_id=request.user.id).first()
    user = User.objects.filter(username=request.user).first()
    if request.method == 'POST':
        form_user = EditUserForm(data=request.POST)
        form_extended = EditProfileForm(data=request.POST)
        if form_user.is_valid() and form_extended.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            profile.img = request.POST['img']
            profile.phone = request.POST['phone']
            profile.address = request.POST['address']
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
    })