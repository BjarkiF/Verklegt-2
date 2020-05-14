from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from . import forms

urlpatterns = [
    path('', views.index, name="Management Index"),
    path('groups/', views.groups, name="Groups"),
    path('groups/add/', views.groups, name="Groups Add"),
    path('groups/<str:group_name>/', views.group_view, name="Group view"),
    path('groups/<str:group_name>/delete/', views.group_delete, name="Group delete"),
    path('customers/', views.customers, name="Customers"),
    path('customers/<str:username>/', views.employees_profile, name="Customer Profile"),
    path('customers/<str:username>/delete/', views.employees_delete, name="Customer Profile"),
    path('orders/', views.orders, name="Orders"),
    path('orders/<int:id>', views.orders_details, name="Order Details"),
    path('orders/<int:id>/delete/', views.orders_delete, name="Order Delete"),
    path('employees/', views.employees, name="Employees"),
    path('employees/<str:username>/', views.employees_profile, name="Employee Profile"),
    path('employees/register/', views.employees_register, name="Register Employee"),
    path('config/', views.config, name="Management Config"),
]