from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img = models.CharField(max_length=999, default='', blank=True, verbose_name='Mynd')
    address = models.CharField(max_length=255, verbose_name='Heimilisfang *', blank=True)
    phone = models.CharField(max_length=999, default='', blank=True, verbose_name='Símanúmer')


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)