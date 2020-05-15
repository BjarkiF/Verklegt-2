from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name="Login"),
    path('register/', views.register, name="Register"),
    path('reset/', views.recover, name="Recover"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="Logout"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name="Login"),
    path('profile/edit', views.edit_profile, name="Edit_profile"),
    path('profile/', views.profile, name="Profile"),
    path('profile/address/', views.edit_address, name='Edit_address'),
    path('profile/search/', views.get_search_history, name='profile_search_history'),
    path('profile/orders/', views.get_order_history, name='profile_order_history'),
    path('profile/orders/<int:id>/', views.order_details, name='profile_order_details'),
    path('profile/search/delete/', views.search_history_delete, name='delete_search_history'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_sent.html'), name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/login.html'), name='password_reset_complete'),
]