from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('removeall/<int:id>/', views.remove_from_cart_all, name='remove_from_cart_all'),
    path('checkout/', views.checkout),
    path('review/', views.review),
    path('confirm/', views.confirm, name='confirm_order'),

]