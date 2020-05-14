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
    path('', LoginView.as_view(template_name='users/login.html'), name="Login"),
    path('register/', views.register, name="Register"),
    path('reset/', views.recover, name="Recover"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="Login"),
    path('profile/edit', views.edit_profile, name="Edit_profile"),
    path('profile/', views.profile, name="Profile"),
    path('reset/<str:token>/', auth_views.PasswordResetView, name='password_reset_confirm'), # TODO: Password reset
    path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
    path('profile/address/', views.edit_address, name='Edit_address')
]