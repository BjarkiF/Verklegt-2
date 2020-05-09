from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path('items/all/', views.items.as_view({'get': 'list'})),
    path('<int:id>', views.get_item_by_id)
]
