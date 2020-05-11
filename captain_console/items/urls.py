from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path('<int:id>', views.get_item_by_id),
    path('filter/<int:id>', views.get_items_category)
]