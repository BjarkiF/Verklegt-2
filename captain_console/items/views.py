from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item, ItemManufacturer, ItemCategory
from items.forms.forms import EditItemForm
from users.models import UserItemSearch
from cart.views import get_cart_items
import datetime


def edit(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form_item = EditItemForm(data=request.POST)
        if form_item.is_valid():
            item.price = request.POST['price']
            item.description = request.POST['description']
            item.save()
            return get_item_by_id(request, id)
    return render(request, 'items/edit_item.html', context={

            'form_item': EditItemForm(instance=item),
            'item': Item.objects.get(id=id)

    })


def delete(request, id):
    Item.objects.get(id=id).delete()
    return all_items(request)


def index(request):
    return render(request, 'items/index.html')


# manuf í context er til að fá lista af framleiðendum í sidebar filter
def all_items(request):

    # Ef það er query string í URL þá áframsendist requestið á filter fallið
    if request.GET.get('filter-cat') or request.GET.get('filter-sort') or request.GET.get('filter-manuf'): #gera betur?
        return get_items_filter(request)
    try:
        session_check = request.session['search_ids']
    except KeyError:
        session_check = None
    if session_check:
        ids = request.session['search_ids']
        request.session['search_ids'] = None
        items = Item.objects.filter(id__in=ids)
        context = {
        'items': items,
        'manuf': ItemManufacturer.objects.all().order_by('name')
        }
    else:
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
        'items': Item.objects.filter(category_id=id),
        'manuf': ItemManufacturer.objects.all().order_by('name'),
    }
    return render(request, 'items/all_items.html', context)


# Tékkar hvað er í query strengnum og býr til filteraðan lista eftir því
def get_items_filter(request):
    try:
        category = ItemCategory.objects.get(name=request.GET.get('filter-cat'))
    except ItemCategory.DoesNotExist:
        category = None
    try:
        manuf = ItemManufacturer.objects.get(name=request.GET.get('filter-manuf'))
    except ItemManufacturer.DoesNotExist:
        manuf = None
    sort = request.GET.get('filter-sort')

    if category:
        if manuf:
            items = Item.objects.filter(category_id=category.id, manufacturer_id=manuf.id).order_by('name')
        else:
            items = Item.objects.filter(category_id=category.id).order_by('name')
        if sort:
            items = items.order_by(str(sort))
    elif manuf:
        items = Item.objects.filter(manufacturer_id=manuf.id).order_by('name')
        if sort:
            items = items.order_by(str(sort))
    else:
        items = Item.objects.all().order_by(str(sort))

    manuf_context = ItemManufacturer.objects.all().order_by('name')
    context = {
        'items': items,
        'manuf': manuf_context,
    }
    return render(request, 'items/all_items.html', context)


def search(request):
    search_term = request.GET.get('q')
    if not request.user.is_anonymous:
        dupe_check = len(UserItemSearch.objects.filter(user_id=request.user.id, search=search_term,
                                                       date=datetime.datetime.now()))
        if dupe_check == 0:
            UserItemSearch.objects.create(user_id=request.user.id, search=search_term, date=datetime.datetime.now())
    try:
        manufacturer = ItemManufacturer.objects.get(name=search_term.capitalize())
        items = Item.objects.filter(Q(name__icontains=search_term) | Q(manufacturer_id=manufacturer.id))
    except ItemManufacturer.DoesNotExist:
        items = Item.objects.filter(name__icontains=search_term)
    item_ids = []
    for item in items:
        item_ids.append(item.id)
    request.session['search_ids'] = item_ids
    return redirect('/items/all')
    #return render(request, 'items/all_items.html', {'items': items})
