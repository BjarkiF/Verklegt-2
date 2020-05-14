from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ab"),
 ]