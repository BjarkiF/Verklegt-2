from django.contrib.auth.models import User, Group
from rest_framework import serializers
from items.models import Item, ItemCategory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category', 'price', 'manufacturer']



