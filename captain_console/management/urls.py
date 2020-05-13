from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from . import forms

'''
,
                               authentication_form=forms.UserLoginForm
'''

urlpatterns = [
    path('', views.index, name="Management Index"),
    path('orders/', views.orders, name="Management Orders"),
    path('staff/', views.staff, name="Management Staff"),
    path('staff/register/', views.staffRegister, name="Management Staff"),
    path('config/', views.config, name="Management Config"),
]