"""captain_console URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView

from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings

import os
import logging

from . import views

router = routers.DefaultRouter()
router.register(r'items', include('items.views'), basename='items')


urlpatterns = [
    path('', include('items.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('users/', include('users.urls')),
    path('about/', include('about.urls')),
    path('management/', include('management.urls')),
    path('cart/', include('cart.urls')),
    path('api/v1/', include('api.urls')),
]


handler404 = 'captain_console.views.error_404'
handler500 = 'captain_console.views.error_500'
handler403 = 'captain_console.views.error_403'
handler400 = 'captain_console.views.error_400'



logging.info('STATIC_ROOT: {0}'.format(settings.STATIC_ROOT))
