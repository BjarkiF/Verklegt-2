from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Config(models.Model):
    hours_weekdays = models.CharField(max_length=255)
    hours_saturday = models.CharField(max_length=255)
    hours_sunday = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    social_facebook = models.CharField(max_length=255)
    social_twitter = models.CharField(max_length=255)
    social_youtube = models.CharField(max_length=255)
    social_instagram = models.CharField(max_length=255)
    about = models.TextField()
    location = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    zoom = models.IntegerField()
