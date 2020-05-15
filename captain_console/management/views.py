from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#from users.models import Profile
#from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from management.forms.forms import ConfigForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

import logging


def only_staff(user):
    return user.groups.filter(name='staff').count()


def only_employee(user):
    return user.groups.filter(name='employees').count()


# TODO: segja user að hann hafi ekki aðgang  ef hann er loggaður inn sem customer.

@user_passes_test(only_employee)
@login_required
def index(request):
    # TODO: Connect to database.
    data = {
        'active_page': 'index',
        'orders': {
            'unprocesessed': 1337,
            'ready': 7,
            'mailed': 666
        },
        'customers': {
            'customers_registered': 31337,
            'customers_online': 42
        },
        'top10_items':[
            {'name':'Hlutur1', 'sold': 33},
            {'name':'Hlutur2', 'sold': 55},
            {'name':'Hlutur3', 'sold': 22},
            {'name':'Hlutur4', 'sold': 11},
            {'name':'Hlutur5', 'sold': 66},
        ],
        'reviews': [
            { 'username':'Jónas', 'text': 'Review texti 1' },
            { 'username':'Jónas', 'text': 'Review texti 2' },
            { 'username':'Jónas', 'text': 'Review texti 3' },
            { 'username':'Jónas', 'text': 'Review texti 4' }
        ]
    }
    return render(request, 'management/index.html', data)


@user_passes_test(only_employee)
@login_required
def orders(request):
    # orders = Orders.objects.all()
    # TODO: Connect to database.
    data = [
        {'id': 0, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 2},
        {'id': 1, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'id': 2, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 3},
        {'id': 3, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'id': 4, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1},
        {'id': 5, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}
    ]
    return render(request, 'management/orders/index.html', {'orders': data, 'active_page': 'orders',})


@user_passes_test(only_employee)
@login_required
def orders_details(request):
    # orders = Orders.objects.all()
    # TODO: Connect to database.
    data = {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}

    return render(request, 'management/orders/order.html', {'order': data, 'active_page': 'orders',})


@user_passes_test(only_employee)
@login_required
def orders_delete(request, id):
    # orders = Orders.objects.all()
    # TODO: Connect to database.
    data = {'id': id, 'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}
    logging.info('Deleting order ID: {0}'.format(id))
    return redirect('/management/orders/')


@user_passes_test(only_employee)
@login_required
def employees(request):
    data = User.objects.filter(is_staff='t').order_by('first_name')
    return render(request, 'management/employees/index.html', {'staff': data, 'active_page': 'employees',})


@user_passes_test(only_employee)
@login_required
def employees_profile(request, username):
    data = User.objects.filter(is_staff='t', username=username)
    return render(request, 'management/employees/details.html', {'employee': data, 'active_page': 'employees',})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def employees_register(request):
    # TODO: Connect to database.
    return render(request, 'management/employees/register.html', { 'active_page': 'employees', })


#@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def user_delete(request, username):
    # TODO: Connect to database.
    logging.info('Deleting Account Username: {0}'.format(username))

    User.objects.filter(username=username).delete()

    return redirect(request.GET.get('next'))

#@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def user_lock(request, username):
    # TODO: Connect to database.
    logging.info('Locking Account Username: {0}'.format(username))
    logging.info('Next: {0}'.format(request.GET.get('next')))

    u = User.objects.get(username=username)

    logging.info('is_active: {0}'.format(u.is_active))

    if u.is_active == True:
        u.is_active = False
    else:
        u.is_active = True
    u.save()

    return redirect(request.GET.get('next'))


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

    #active_page = request.path.split('/')
    #logging.info(active_page)

    return render(request, 'management/config.html', {'config': data, 'active_page': 'config', 'footer-form': ConfigForm()})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def groups(request):
    data = Group.objects.all().order_by('name')
    #for g in groups:
    #    l = request.user.groups.values_list('name', flat=True)  # QuerySet Object
    #    l_as_list = list(l)  # QuerySet to `list`
    #    users = User.objects.filter()
    #    logging.info('Group: {0}, User Groups: {1} Users: {2}'.format(g, l_as_list, {'users': users}))

    return render(request, 'management/groups/index.html', {'groups': data, 'active_page': 'groups',})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def group_delete(request, group_name):
    data = Group.objects.all()
    logging.info('Delete Group: {0}'.format(group_name))
    #for g in groups:
    #    l = request.user.groups.values_list('name', flat=True)  # QuerySet Object
    #    l_as_list = list(l)  # QuerySet to `list`
    #    users = User.objects.filter()
    #    logging.info('Group: {0}, User Groups: {1} Users: {2}'.format(g, l_as_list, {'users': users}))

    return redirect('/management/groups/')


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def group_view(request, group_name):
    data = Group.objects.filter(name=group_name)
    #for g in groups:
    #    l = request.user.groups.values_list('name', flat=True)  # QuerySet Object
    #    l_as_list = list(l)  # QuerySet to `list`
    #    users = User.objects.filter()
    #    logging.info('Group: {0}, User Groups: {1} Users: {2}'.format(g, l_as_list, {'users': users}))

    return render(request, 'management/groups/details.html', {'group': data, 'active_page': 'groups',})


@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def group_new(request):
    data = {}
    logging.info('New group!')
    #for g in groups:
    #    l = request.user.groups.values_list('name', flat=True)  # QuerySet Object
    #    l_as_list = list(l)  # QuerySet to `list`
    #    users = User.objects.filter()
    #    logging.info('Group: {0}, User Groups: {1} Users: {2}'.format(g, l_as_list, {'users': users}))

    return render(request, 'management/groups/new.html', {'group': data, 'active_page': 'groups',})


@user_passes_test(only_employee)
@login_required
def customers(request):
    data = User.objects.filter(is_staff='f').order_by('first_name')
    return render(request, 'management/customers/index.html', {'customers': data, 'active_page': 'customers',})



@user_passes_test(only_employee)
@login_required
def customers_details(request, username):
    data = User.objects.filter(is_staff='f', username=username)
    return render(request, 'management/customers/details.html', {'customer': data, 'active_page': 'customers',})
