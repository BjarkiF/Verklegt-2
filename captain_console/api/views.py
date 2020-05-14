from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from users.forms.forms import EditProfileForm, RegisterForm, EditUserForm
from items.models import Item, ItemManufacturer
from cart.models import Cart
from users.models import User#, Users
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import ItemSerializer, UserSerializer

"""
def index(request):
    data = {
        'name': 'API INDEX x_X'
    }
    return JsonResponse(data)


def all(request):
    context = {
        'items': Item.objects.all().order_by('name'),
        'manuf': ItemManufacturer.objects.all().order_by('name')
    }
    #return JsonResponse({context})
    return JsonResponse(json.dumps(context))


def get_item_by_id(request):
    data = {
        'name': 'BY ID x_X'
    }
    return JsonResponse(data)
"""


class item(viewsets.ModelViewSet):
    """
    TODO: rename this
    Return items in the store.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Items(viewsets.ModelViewSet):
    """
    Return items in the store.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Cart(viewsets.ModelViewSet):
    """
    Returns user cart.
    """
    queryset = Cart.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class user(viewsets.ModelViewSet):
    """
    TODO: rename this
    Return user profile..
    """
    queryset = User.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class Users(viewsets.ModelViewSet):
    """
    Returns all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
