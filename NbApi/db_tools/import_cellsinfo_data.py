# # -*- coding: utf-8 -*-
# # @Time : 2020年02月19日 17时47分
# # @Email : 15669909922@163.com
# # @Author : HuangChuan
# # @File : import_basecommsites_data.py
# # @notice ：
#
#
# # 独立使用django的model
# import sys
# import os
# import pandas as pd
# import numpy as np
# from django.db.models import Q
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
# df = pd.read_excel('./data/cellinfo.xlsx')
# arr = np.array(df)
# for data in arr:
#
#     # if len(CellsInfo.objects.filter(Q(eci=data[7])&Q(azimuth=data[17]))) == 0:
#     table = CellsInfo()
#     table.dist = data[0]
#     table.city = data[1]
#     table.site_name = data[2]
#     table.cell_name = data[3]
#     table.site_id = data[4]
#     table.enbid = data[5]
#     table.local_cell_id = data[6]
#     table.eci = data[7]
#     table.physical_cell_id = data[8]
#     table.pci_mod3 = data[9]
#     table.tac = data[10]
#     table.longitude = data[11]
#     table.latitude = data[12]
#     table.frequency_band = data[13]
#     table.frequency_point = data[14]
#     table.bandwidth = data[15]
#     table.site_type = data[16]
#     table.azimuth = data[17]
#     table.station_height = data[18]
#     table.total_pitch_angle = data[19]
#     table.inner_pitch_angle = data[20]
#     table.electronic_pitch_angle = data[21]
#     table.mechanical_pitch_angle = data[22]
#     table.sprod_name = data[23]
#     table.grid_info = data[24]
#     table.band_type = data[25]
#     table.common_site_name = data[26]
#     table.sector = data[27]
#
#     table.parent_level = CellsLevel.objects.filter(name = data[27])[0]
#
#     table.save()
#
#         # lev1_instance = CellsLevel()
#         # exists = CellsLevel.objects.filter(name=data[26],level_type=1)
#         # if not exists:
#         #     lev1_instance.name = data[26]
#         #     lev1_instance.level_type = 1
#         #     lev1_instance.save()
#         #
#         # exists = CellsLevel.objects.filter(name=data[2], level_type=2)
#         # if not exists:
#         #     lev2_instance = CellsLevel()
#         #     lev2_instance.name = data[2]
#         #     lev2_instance.level_type = 2
#         #     lev2_instance.parent_level = CellsLevel.objects.filter(name = data[26])[0]
#         #     lev2_instance.save()
#         #
#         # exists = CellsLevel.objects.filter(name=data[27], level_type=3)
#         # if not exists:
#         #     lev3_instance = CellsLevel()
#         #     lev3_instance.name = data[27]
#         #     lev3_instance.level_type = 3
#         #     lev3_instance.parent_level = CellsLevel.objects.filter(name = data[2])[0]
#         #     lev3_instance.save()
#
#         # _parent_level = CellsLevel.objects.get(name = data[27])
#         # CellsInfo.objects.filter(sector = data[27]).update(parent_level=_parent_level)