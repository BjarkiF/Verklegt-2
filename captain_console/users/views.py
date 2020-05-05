from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from users.forms.profile_form import ProfileForm
from users.models import Users


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    return render(request, 'users/register.html', {
        'form': UserCreationForm()
    })

def edit_profile(request):
    profile = Users.objects.filter(user=request.user).first()
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

def profile(request):
    return render(request, 'users/profile.html', {
        'user': Users.objects.filter(user=request.user).first()
    })