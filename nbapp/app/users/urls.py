# coding:utf-8

from django.urls import path
from .auth import Login, Regist, LogoutUser

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('regist', Regist.as_view(), name='regist'),
    path('logout', LogoutUser.as_view(), name='logout'),
]
