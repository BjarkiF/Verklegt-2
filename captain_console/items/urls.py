from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

# app_name = 'items'

urlpatterns = [
    path('', views.index),
    path('all/', views.all),
    path(r'^all/$', views.get_items_filter), # TODO: færa þetta í REST API.
    path('<int:id>', views.get_item_by_id),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'),  name="Logout"),
    path('login', LoginView.as_view(template_name='registration/login.html'), name="Login"),
    path('filter/<int:id>', views.get_items_category),
    path('search/', views.search)
]