from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test

#from users.models import Profile
from cart.models import Order
from users.forms.forms import RegisterForm
from items.forms.forms import CreateItemForm
from items.models import Item, ItemImg
from config.models import Config

from management.forms.forms import ConfigForm

import logging
import datetime


def only_staff(user):
    return user.groups.filter(name='staff').count()


def only_employee(user):
    return user.groups.filter(name='employees').count()


# TODO: segja user að hann hafi ekki aðgang  ef hann er loggaður inn sem customer.
@user_passes_test(only_employee)
@login_required
def index(request):
    orders = Order.objects.all()
    context ={
        'orders_ready': orders.filter(complete=True).count(),
        'orders_not': orders.filter(complete=False).count(),
        'accounts': User.objects.all().count(),
        'accounts_active': User.objects.filter(is_active=True).count(),
        'active_page': 'index'
    }
    return render(request, 'management/index.html', context)


@user_passes_test(only_employee)
@login_required
def orders(request):
    orders = Order.objects.filter(complete=False)
    context ={
        'orders': orders,
        'active_page': 'orders'
    }
    return render(request, 'management/orders/index.html', context)


# @user_passes_test(only_employee)
# @login_required
# def orders_details(request):
#     # orders = Orders.objects.all()
#     # TODO: Connect to database.
#     data = {'name': 'Kristinn Jónsson', 'city': 'Reykjavík', 'count': 1}
#
#     return render(request, 'management/orders/order.html', {'order': data, 'active_page': 'orders',})


@user_passes_test(only_employee)
@login_required
def orders_delete(request, id):
    Order.objects.get(id=id).delete()
    logging.info('Deleting order ID: {0}'.format(id))
    return redirect('/management/orders/')


def orders_complete(request, id):
    order = Order.objects.get(id=id)
    order.complete = True
    order.save()
    logging.info('Completing order ID: {0}'.format(id))
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
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            user.is_staff = True
            user.save()
            return redirect('/management/employees')
    context ={
        'form': RegisterForm(),
        'active_page': 'employees',
    }
    return render(request, 'management/employees/register.html', context)


#@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def user_delete(request, username):
    logging.info('Deleting Account Username: {0}'.format(username))

    User.objects.filter(username=username).delete()

    return redirect(request.GET.get('next'))

#@user_passes_test(only_employee)
@user_passes_test(only_staff)
@login_required
def user_lock(request, username):
    logging.info('Locking Account Username: {0}'.format(username))
    logging.info('Next: {0}'.format(request.GET.get('next')))

    u = User.objects.get(username=username)
    if username != request.user.username:
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
    if request.method == 'POST':
        form = ConfigForm(data=request.POST)
        if form.is_valid():
            config_new = Config.objects.create(
                hours_weekdays=request.POST.get('hours_weekdays'),
                hours_saturday=request.POST.get('hours_saturday'),
                hours_sunday=request.POST.get('hours_sunday'),
                email =request.POST.get('email'),
                telephone=request.POST.get('telephone'),
                address=request.POST.get('address'),
                social_facebook=request.POST.get('social_facebook'),
                social_twitter=request.POST.get('social_twitter'),
                social_instagram=request.POST.get('social_instagram'),
                about=request.POST.get('about'),
                location=request.POST.get('location')
            )
            config_new.save()

            return redirect('/management/config/')
        else:
            logging.error('Config form is not valid!')
            return redirect('/management/config/')
    else:
        try:
            c = Config.objects.last()
            logging.info('object:')
            logging.info(c)
        except:
            logging.info('No config set!')

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

        logging.info(dir(ConfigForm()))

    return render(request, 'management/config.html', {'config': data, 'active_page': 'config', 'form': ConfigForm()})


# @user_passes_test(only_employee)
# @user_passes_test(only_staff)
# @login_required
# def groups(request):
#     data = Group.objects.all().order_by('name')
#
#     return render(request, 'management/groups/index.html', {'groups': data, 'active_page': 'groups',})


# @user_passes_test(only_employee)
# @user_passes_test(only_staff)
# @login_required
# def group_delete(request, group_name):
#     data = Group.objects.all()
#     logging.info('Delete Group: {0}'.format(group_name))
#
#     return redirect('/management/groups/')


# @user_passes_test(only_employee)
# @user_passes_test(only_staff)
# @login_required
# def group_view(request, group_name):
#     data = Group.objects.filter(name=group_name)
#
#     return render(request, 'management/groups/details.html', {'group': data, 'active_page': 'groups',})


# @user_passes_test(only_employee)
# @user_passes_test(only_staff)
# @login_required
# def group_new(request):
#     data = {}
#     logging.info('New group!')
#
#     return render(request, 'management/groups/new.html', {'group': data, 'active_page': 'groups',})


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


@user_passes_test(only_employee)
@login_required
def new_item(request):
    if request.method == 'POST':
        form = CreateItemForm(data=request.POST)
        if form.is_valid():
            item_temp = Item.objects.create(
                id = (int(Item.objects.latest('id').id) + 1),
                name=request.POST['name'],
                description=request.POST['description'],
                price=request.POST['price'],
                manufacturer_id=request.POST['manufacturer_id'],
                category_id=request.POST['category_id'],
                date=datetime.datetime.now()
            )
            item_temp.save()
            img_temp = ItemImg.objects.create(
                id=(int(ItemImg.objects.latest('id').id) + 1),
                item_id=item_temp.id,
                img=request.POST['img']
            )
            img_temp.save()
            return redirect('Management Index')
    context = {
        'form': CreateItemForm(),
        'active_page': 'new_item',
    }
    return render(request, 'management/items/new_item.html', context)
