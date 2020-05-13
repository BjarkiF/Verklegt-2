from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserAddress(models.Model):
    street_name = models.CharField(max_length=999, default='', blank=True)
    house_num = models.CharField(max_length=255, default='', blank=True)
    city = models.CharField(max_length=999, default='', blank=True)
    country = models.CharField(max_length=999, default='', blank=True)
    zipcode = models.CharField(max_length=255, default='', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    # TODO: Hvað er þetta? Eitthvað gamalt?
    # þetta er profile model sem extendar django user modelið svo það sé hægt að geyma myndir, address o.fl.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=999, default='', blank=True, verbose_name='Mynd')
    phone = models.CharField(max_length=999, default='', blank=True, verbose_name='Símanúmer')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)

def create_user_address(sender, instance, created, **kwargs):
    if created:
        UserAddress.objects.create(user=instance)
post_save.connect(create_user_address, sender=User)