from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'management/index.html', {'order_count': 1337})


@login_required
def orders(request):
    #orders = Orders.objects.all()
    orders = [
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 2},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 3},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}
    ]
    return render(request, 'management/orders.html', {'orders': orders})


@login_required
def staff(request):
    staff = Profile.objects.all()
    staff2 = [
        {'name': 'Jón Jónsson', 'kennitala': '000000-0000', 'telephone': '555-1336'},
        {'name': 'Jón Jónsson', 'kennitala': '000000-0000', 'telephone': '555-1337'},
        {'name': 'Jón Jónsson', 'kennitala': '000000-0000', 'telephone': '555-1338'},
    ]
    return render(request, 'management/staff/index.html', {'staff': staff, 'staff2': staff})

@login_required
def staffRegister(request):
    return render(request, 'management/staff/register.html')

@login_required
def config(request):
    config = None
    return render(request, 'management/config.html', {'config': config})
