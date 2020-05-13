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
    # TODO: Hvað er þetta? Eitthvað gamalt?
    # þetta er profile model sem extendar django user modelið svo það sé hægt að geyma myndir, address o.fl.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=999, default='', blank=True, verbose_name='Mynd')
    phone = models.CharField(max_length=999, default='', blank=True, verbose_name='Símanúmer')


class UserCard(models.Model):
    name = models.CharField(max_length=999)
    number = models.IntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvc = models.IntegerField()

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

def create_user_address(sender, instance, created, **kwargs):
    if created:
        UserAddress.objects.create(user=instance)
post_save.connect(create_user_address, sender=User)
