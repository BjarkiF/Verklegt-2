from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

# app_name = 'items'

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path(r'^all/$', views.get_items_filter), # TODO: færa þetta í REST API.
    path('<int:id>', views.get_item_by_id),
    path('login', LoginView.as_view(), name="Login"),
    path('logout', LogoutView.as_view(), name="Logout"),
    path('filter/<int:id>', views.get_items_category),
    path('search/', views.search)
]