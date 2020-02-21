# # -*- coding: utf-8 -*-
# # @Time : 2020年02月20日 21时37分
# # @Email : 15669909922@163.com
# # @Author : HuangChuan
# # @File : delete_data.py
# # @notice ：
#
# # 独立使用django的model
# import sys
# import os
# import pymysql
# import pandas as pd
# import numpy as np
#
# #  获取当前文件的路径，以及路径的父级文件夹名
# pwd = os.path.dirname(os.path.realpath(__file__))
# # 将项目目录加入setting
# sys.path.append(pwd + "../")
# # manage.py中
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NbApi.settings")
#
# import django
# django.setup()
# # 这行代码必须在初始化django之后
# from ecels.models import CellsInfo, CellsLevel
#
# # conn = pymysql.connect(host="127.0.0.1", user="root",password="123456",database="nbapp2",charset="utf8")
# # cursor = conn.cursor()
# #
# # sql = 'select eci from ecels_cellsinfo GROUP BY eci HAVING COUNT(*)>1'
# # cursor.execute(sql)
# # results = cursor.fetchall()
# l = ['69131',
# '69132',
# '69133',
# '69134',
# '69135',
# '69136',
# '69137',
# '69138',
# '69139',
# '69140',
# '69141',
# '69142',
# '69143',
# '69144',
# '69145',
# '69146',
# '69147',
# '69148',
# '69149',
# '69150',
# '69151',
# '69152',
# '69153',
# '69154',
# '69155',
# '69156',
# '69157',
# '69158'
# ]
# # for i in results:
# #     l.append(i[0])
# CellsInfo.objects.filter(pk__in=l).delete()
#
# # conn.commit()
# # cursor.close()
# # conn.close()