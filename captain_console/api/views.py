from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from items.models import Item, ItemManufacturer
from cart.models import Cart
from django.forms.models import model_to_dict

from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import ItemSerializer

import json

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


class items(viewsets.ModelViewSet):
    """
    #API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class cart(viewsets.ModelViewSet):
    """
    #API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]



