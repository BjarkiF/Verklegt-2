from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserCountry(models.Model):
    country_name = models.CharField(max_length=999)


class UserAddress(models.Model):
    street_name = models.CharField(max_length=999, default='')
    house_num = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=999, default='')
    country = models.ForeignKey(UserCountry, on_delete=models.CASCADE, default=100)
    zipcode = models.CharField(max_length=255, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=999, default='', blank=True, verbose_name='Mynd')
    phone = models.CharField(max_length=999, default='', blank=True, verbose_name='Símanúmer')


class UserCard(models.Model):
    name = models.CharField(max_length=999)
    number = models.CharField(max_length=16)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=2)
    cvc = models.CharField(max_length=3)


class UserItemSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=999)
    date = models.DateField()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

def create_user_address(sender, instance, created, **kwargs):
    if created:
        UserAddress.objects.create(user=instance)
post_save.connect(create_user_address, sender=User)
