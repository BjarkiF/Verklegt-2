from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from items.models import Item, ItemManufacturer

def index(request):
    return render(request, 'items/index.html')

def all(request):
    items = []
    if 'search_filter' in request.GET:  #TODO: search virkar ekki
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'img': x.itemimg_set.first.img,
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})
    context = {
        'items': Item.objects.all().order_by('name'),
        'manuf': ItemManufacturer.objects.all().order_by('name')
    }
    return render(request, 'items/all_items.html', context)

def get_item_by_id(request, id):
    return render(request, 'items/single_item_detail.html', {
        'item': get_object_or_404(Item, pk=id)
    })

def get_items_category(request, id):
    context = {
        'items': Item.objects.filter(category_id=id)
    }
    return render(request, 'items/all_items.html', context)