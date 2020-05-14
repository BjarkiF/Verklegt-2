from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

import logging


def only_staff(user):
    return user.groups.filter(name='staff').count()


def only_employee(user):
    return user.groups.filter(name='employees').count()


# TODO: Gera bash scriptu sem setur upp nokkra mismuandi notendur.
# TODO: Setja inn roles í Users. Bara ákveðin role eiga að getað skoðað þessa síðu.
# TODO: nota is_superuser og is_staff flöggin til að stýra hvað hver getur gert.
# superuser getur verið með is_staff = f og ekki komið fram á staff síðunni
# venjulegir users koma heldur ekki á þeirri síðu.


@user_passes_test(only_employee)
@login_required
def index(request):
    # TODO: Connect to database.
    data = {'orders': {'unprocesessed': 1337, 'ready': 42, 'mailed': 666}}
    return render(request, 'management/index.html', data)


@user_passes_test(only_employee)
@login_required
def orders(request):
    # orders = Orders.objects.all()
    # TODO: Connect to database.
    data = [
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 2},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 3},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}
    ]
    return render(request, 'management/orders.html', {'orders': data})


@user_passes_test(only_employee)
@login_required
def staff(request):
    data = User.objects.filter(is_staff='t')
    return render(request, 'management/staff/index.html', {'staff': data})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def staff_register(request):
    # TODO: Connect to database.
    return render(request, 'management/staff/register.html')


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def config(request):
    # TODO: Sumir notendur eiga að sjá config og getað breytt meðal annars upplýsingum í footernum.
    # Config example
    data = {
        'footer': {
            'opening_hours': [
                'Mon-Fri: 10:00 - 18:00',
                'Lau: 12:00 - 17:00',
                'Sun: 13:00 - 16:00'
            ],
            'contact': {
                'email':'verslun@captain.is',
                'telephone': '581-2345',
                'address': 'Gamergata 14, Kópavogur'
            },
            'social': [
                'facebook.com/CaptainConsole',
                'instagram.com/CaptainConsole',
                'twitter.com/CaptainConsole'
            ]
        }
    }
    return render(request, 'management/config.html', {'config': data})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def groups(request):
    data = Group.objects.all()
    for g in groups:
        l = request.user.groups.values_list('name', flat=True)  # QuerySet Object
        l_as_list = list(l)  # QuerySet to `list`
        users = User.objects.filter(groups__name='customers')
        logging.info('Group: {0}, User Groups: {1} Users: {2}'.format(g, l_as_list, {'users': users}))

    return render(request, 'management/groups.html', {'groups': data})


@user_passes_test(only_employee)
@login_required
def customers(request):
    data = User.objects.filter(is_staff='f')
    return render(request, 'management/customers.html', {'customers': data})

