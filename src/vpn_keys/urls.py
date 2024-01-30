"""
URL configuration for vpn_keys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.static import serve
from django.contrib import admin
from django.urls import path

from outline_users.views import OutlineKeysView, KeyForOutline

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-key/', OutlineKeysView.as_view()),
    path('post-key/<int:pk>', OutlineKeysView.as_view()),
    path('get-client-key/<int:pk>', KeyForOutline.as_view()),
]

