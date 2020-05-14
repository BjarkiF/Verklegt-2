from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test


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


@user_passes_test(only_employee)
@login_required
def staff(request):
    staff = User.objects.filter(is_staff='t')
    return render(request, 'management/staff/index.html', {'staff': staff})


@user_passes_test(only_employee)
@login_required
def staffRegister(request):
    # TODO: Connect to database.
    return render(request, 'management/staff/register.html')


@user_passes_test(only_employee)
@login_required
def config(request):
    # TODO: Sumir notendur eiga að sjá config og getað breytt meðal annars upplýsingum í footernum.
    config = None
    return render(request, 'management/config.html', {'config': config})


@user_passes_test(only_employee)
@login_required
def groups(request):
    groups = Group.objects.all()
    return render(request, 'management/groups.html', {'groups': groups})


@user_passes_test(only_employee)
@login_required
def customers(request):
    customers = User.objects.filter(is_staff='f')
    return render(request, 'management/customers.html', {'customers': customers})

