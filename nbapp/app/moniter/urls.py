# coding:utf-8

from django.urls import path
from .views import MoniterPage

urlpatterns = [
    path('moniter', MoniterPage.as_view(), name='moniter'),
]
