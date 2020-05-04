from django.shortcuts import render, get_object_or_404
from items.models import Item

def index(request):
    return render(request, 'items/index.html')

def all(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'items/all_items.html', context)

def get_item_by_id(request, id):
    return render(request, 'items/single_item_detail.html', {
        'item': get_object_or_404(Item, pk=id)
    })