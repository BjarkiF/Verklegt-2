from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index),
    #path('all/', views.all),
    path('items/<int:id>', views.item.as_view({'get': 'list'})),
    path('items/all', views.Items.as_view({'get': 'list'})),
    path('cart', views.Cart.as_view({'get': 'list'})),
    path('user/<int:id>', views.user.as_view({'get': 'list'})),
    path('users', views.Users.as_view({'get': 'list'})),
    #path('<int:id>', views.get_item_by_id)
]
