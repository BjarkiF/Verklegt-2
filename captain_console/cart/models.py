from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=255))
