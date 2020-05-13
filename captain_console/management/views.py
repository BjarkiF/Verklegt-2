from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from django.contrib.auth.models import User

# TODO: Setja inn roles í Users. Bara ákveðin role eiga að getað skoðað þessa síðu.

@login_required
def index(request):
    # TODO: Connect to database.
    data = {'orders': {'unprocesessed': 1337, 'ready': 42, 'mailed': 666}}
    return render(request, 'management/index.html', data)


@login_required
def orders(request):
    #orders = Orders.objects.all()
    # TODO: Connect to database.
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
    staff = User.objects.filter(is_superuser='f')
    return render(request, 'management/staff/index.html', {'staff': staff})


@login_required
def staffRegister(request):
    # TODO: Connect to database.
    return render(request, 'management/staff/register.html')


@login_required
def config(request):
    # TODO: Sumir notendur eiga að sjá config og getað breytt meðal annars upplýsingum í footernum.
    config = None
    return render(request, 'management/config.html', {'config': config})