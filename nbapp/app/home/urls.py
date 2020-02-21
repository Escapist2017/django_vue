# coding:utf-8

from django.urls import path
from .views import HomePage

urlpatterns = [
    path('home', HomePage.as_view(), name='home'),
]
