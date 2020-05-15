from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import UserAddress, UserCard
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=255, blank=True))

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=255))
    total = models.CharField(max_length=255)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    date = models.DateField()
