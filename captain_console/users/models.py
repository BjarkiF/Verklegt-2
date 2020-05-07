from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Fornafn *')
    last_name = models.CharField(max_length=255, verbose_name='Eftirnafn *')
    img = models.CharField(max_length=999, default='', blank=True, verbose_name='Mynd')
    email = models.CharField(max_length=255, verbose_name='Netfang *')
    address = models.CharField(max_length=255, verbose_name='Heimilisfang *')
    phone = models.CharField(max_length=999, default='', blank=True, verbose_name='Símanúmer')
