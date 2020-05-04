from django.shortcuts import render
from items.models import Item

def index(request):
    return render(request, 'items/index.html')

def all(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'items/all_items.html', context)
