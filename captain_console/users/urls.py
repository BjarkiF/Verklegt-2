from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='users/index.html'), name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(next_page='/'), name="Logout"),
    path('profile/edit', views.edit_profile, name="Edit_profile"),
    path('profile', views.profile, name="Profile")
]