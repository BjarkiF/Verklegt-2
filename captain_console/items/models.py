from django.db import models
from django.utils import timezone

# TODO: Þarf að skrifa SQL view fyrir sumt?


class ItemCategory(models.Model):
    name = models.CharField(max_length=255) #TODO: skoða parent category?


class ItemManufacturer(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now())
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE) # TODO: Gera frekar nýja töflu eða lista af id?
    price = models.IntegerField()
    manufacturer = models.ForeignKey(ItemManufacturer, on_delete=models.CASCADE)


class ItemImg(models.Model):
    img = models.CharField(max_length=999)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
