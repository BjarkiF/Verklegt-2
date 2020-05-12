from django.urls import path
from . import views

# app_name = 'items'

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path(r'^all/$', views.get_items_filter),
    path('<int:id>', views.get_item_by_id),
    path('filter/<int:id>', views.get_items_category),
]