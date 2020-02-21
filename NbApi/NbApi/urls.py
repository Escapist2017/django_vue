
from django.contrib import admin
import xadmin
from django.urls import path, re_path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from ecels.views import CellsLevelViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cellevs', CellsLevelViewSet)

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', include(router.urls)),
]
