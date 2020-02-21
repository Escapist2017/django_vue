# -*- coding: utf-8 -*-
# @Time : 2020年02月19日 19时00分
# @Email : 15669909922@163.com
# @Author : HuangChuan
# @File : serializers.py
# @notice ：

from rest_framework import serializers
from .models import CellsLevel, CellsInfo

class CellsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CellsInfo
        # fields = "__all__"
        fields = ['city','cell_name','enbid','eci']

class CellsLevelSerializer3(serializers.ModelSerializer):
    sub_cells = CellsInfoSerializer(many=True)
    class Meta:
        model = CellsLevel
        # fields = "__all__"
        fields = ['name','sub_cells']

class CellsLevelSerializer2(serializers.ModelSerializer):
    sub_lev = CellsLevelSerializer3(many=True)
    class Meta:
        model = CellsLevel
        # fields = "__all__"
        fields = ['name','sub_lev']

class CellsLevelSerializer(serializers.ModelSerializer):
    sub_lev = CellsLevelSerializer2(many=True)
    class Meta:
        model = CellsLevel
        # fields = "__all__"
        fields = ['name','sub_lev']