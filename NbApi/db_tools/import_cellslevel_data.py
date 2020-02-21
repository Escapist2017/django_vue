# # -*- coding: utf-8 -*-
# # @Time : 2020年02月19日 13时47分
# # @Email : 15669909922@163.com
# # @Author : HuangChuan
# # @File : import_cellslevel_data.py
# # @notice ：
#
# # 独立使用django的model
# import sys
# import os
#
# #  获取当前文件的路径，以及路径的父级文件夹名
# pwd = os.path.dirname(os.path.realpath(__file__))
# # 将项目目录加入setting
# sys.path.append(pwd + "../")
# # manage.py中
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NbApi.settings")
#
# import django
# import pymysql
# django.setup()
#
# # 这行代码必须在初始化django之后
# from ecels.models import CellsLevel
#
# conn = pymysql.connect(host="127.0.0.1", user="root",password="123456",database="nbapp",charset="utf8")
# cursor = conn.cursor()
#
# sql = 'select dist,dist_code from ecels_basecommsites group by dist,dist_code'
# cursor.execute(sql)
# results = cursor.fetchall()
# for lav1 in results:
#     try:
#         lev1_instance = CellsLevel()
#         lev1_instance.name = lav1[0]
#         lev1_instance.code = lav1[1]
#         lev1_instance.level_type = 1
#         lev1_instance.save()
#     except:
#         continue
#
# sql = 'select city,city_code,dist_code from ecels_basecommsites group by city,city_code,dist_code'
# cursor.execute(sql)
# results = cursor.fetchall()
# for lav2 in results:
#     try:
#         lev2_instance = CellsLevel()
#         lev2_instance.name = lav2[0]
#         lev2_instance.code = lav2[1]
#         lev2_instance.level_type = 2
#         lev2_instance.parent_level = CellsLevel.objects.filter(code=lav2[2])[0]
#         lev2_instance.save()
#     except:
#         continue
#
# sql = 'select commsite,commsite_code,city_code from ecels_basecommsites group by commsite,commsite_code,city_code'
# cursor.execute(sql)
# results = cursor.fetchall()
# for lav3 in results:
#     try:
#         lev3_instance = CellsLevel()
#         lev3_instance.name = lav3[0]
#         lev3_instance.code = lav3[1]
#         lev3_instance.level_type = 3
#         lev3_instance.parent_level = CellsLevel.objects.filter(code=lav3[2])[0]
#         lev3_instance.save()
#     except:
#         continue
#
# sql = 'select site,site_code,commsite_code from ecels_basecommsites group by site,site_code,commsite_code'
# cursor.execute(sql)
# results = cursor.fetchall()
# for lav4 in results:
#     try:
#         lev4_instance = CellsLevel()
#         lev4_instance.name = lav4[0]
#         lev4_instance.code = lav4[1]
#         lev4_instance.level_type = 4
#         lev4_instance.parent_level = CellsLevel.objects.filter(code=lav4[2])[0]
#         lev4_instance.save()
#     except:
#         continue
#
# sql = 'select cell,cell_code,site_code from ecels_basecommsites group by cell,cell_code,site_code'
# cursor.execute(sql)
# results = cursor.fetchall()
# for lav5 in results:
#     try:
#         lev5_instance = CellsLevel()
#         lev5_instance.name = lav5[0]
#         lev5_instance.code = lav5[1]
#         lev5_instance.level_type = 5
#         lev5_instance.parent_level = CellsLevel.objects.filter(code=lav5[2])[0]
#         lev5_instance.save()
#     except:
#         continue
#
# conn.commit()
# cursor.close()
# conn.close()