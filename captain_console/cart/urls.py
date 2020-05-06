from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:id>', views.add_to_cart, name='add_to_cart')
]