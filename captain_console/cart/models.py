from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import Users

class Cart(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    items = ArrayField(models.CharField(max_length=255))
