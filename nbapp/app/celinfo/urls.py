# coding:utf-8

from django.urls import path
from .views import CelinfoPage, Cel_Info, Cel_Type, Comm_Site, Comm_Site_update
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('celinfo', CelinfoPage.as_view(), name='celinfo'),
    path('ecellinfo', Cel_Info.as_view(), name='ecellinfo'),
    path('ecelltype', Cel_Type.as_view(), name='ecelltype'),
    path('commsite', Comm_Site.as_view(), name='commsite'),
    path('celinfo/update', csrf_exempt(Comm_Site_update.as_view()), name='celinfo_update'),
]
