# -*- coding: utf-8 -*-
# @Time : 2020年02月19日 19时02分
# @Email : 15669909922@163.com
# @Author : HuangChuan
# @File : filters.py
# @notice ：

from django_filters import rest_framework as filters
from .models import CellsLevel

class CellsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    # 指定字段以及字段上的行为，在shop_price上大于等于
    # pricemin = filters.NumberFilter(name="shop_price", lookup_expr='gte')
    # pricemax = filters.NumberFilter(name="shop_price", lookup_expr='lte')

    class Meta:
        model = CellsLevel
        fields = ['name']
