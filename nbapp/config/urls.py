"""nbapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import xadmin
from app.users import urls as users_urls
from app.home import urls as home_urls
from app.celinfo import urls as celinfo_urls
from app.kpiinfo import urls as kpiinfo_urls
from app.moniter import urls as moniter_urls

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(users_urls)),
    path('', include(home_urls)),
    path('', include(celinfo_urls)),
    path('', include(kpiinfo_urls)),
    path('', include(moniter_urls)),
]
