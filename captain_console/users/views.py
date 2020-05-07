from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms.profile_form import ProfileForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

@login_required
def edit_profile(request):
    profile = User.objects.filter(username=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('Profile')
    return render(request, 'users/edit_profile.html', {
        'form': ProfileForm(instance=profile)
    })

@login_required
def profile(request):
    return render(request, 'users/profile.html', {
        'user': User.objects.filter(username=request.user).first()
    })