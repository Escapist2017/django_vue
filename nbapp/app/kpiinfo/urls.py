# coding:utf-8

from django.urls import path
from .views import KpiinfoPage

urlpatterns = [
    path('kpiinfo', KpiinfoPage.as_view(), name='kpiinfo'),
]
