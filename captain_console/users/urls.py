from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path
from . import views
from .forms import login_form, forms
from django.contrib.auth import views as auth_views
from .forms import forms

urlpatterns = [
    path('', LoginView.as_view(template_name='users/index.html',
                               authentication_form=forms.UserLoginForm), name="Login"),
    path('register', views.register, name="Register"),
    path('reset', views.recover, name="Recover"),
    path('logout', LogoutView.as_view(next_page='/'), name="Logout"),
    path('profile/edit', views.edit_profile, name="Edit_profile"),
    path('profile', views.profile, name="Profile"),
    path('reset/<str:token>/', auth_views.PasswordResetView, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]