from django.contrib.auth.models import User, Group
from rest_framework import serializers
from items.models import Item, ItemCategory
from cart.models import Cart


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category_id', 'price', 'manufacturer_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'items', 'user_id']




