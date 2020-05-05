from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='users/index.html')),
    path('register', views.register),
    path('logout', LogoutView.as_view(next_page='/')),
    path('profile', views.profile)
]