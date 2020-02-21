# coding:utf-8
import xml.etree.cElementTree as ET
from django.db import connection, transaction
import json
import collections
import decimal
from .data2xml import Data_to_xml
import datetime

# 转换Decimal格式
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

# 普通响应数据处理
def response_del(sql,header):
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        objects_dict = {'errorCode': '00', 'errorMsg': '查询成功', 'data': ''}
        objects_list = []
        if rows:
            for x in range(len(rows)):
                d = collections.OrderedDict()
                for y in range(len(header)):
                    d[header[y]] = rows[x][y]
                objects_list.append(d)  # 针对多行
            objects_dict['data'] = objects_list
        else:
            objects_dict['data'] = None  # 如果没数据 返回null
        j = json.dumps(objects_dict, ensure_ascii=False, cls=DecimalEncoder)  # ensure_ascii=False解决中文问题
    except connection.Error as e:
        print(e)
        objects_dict = {'errorCode': '01', 'errorMsg': '{0}'}.__format__(e)
        j = json.dumps(objects_dict, ensure_ascii=False)  # ensure_ascii=False解决中文问题
    return j

# 共站信息数据处理
def response_del_commsite(sql):
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        objects_dict = {'errorCode': '00', 'errorMsg': '查询成功', 'data': {'params':''}}
        if rows:
            x = Data_to_xml()
            xmldata = x.getxml(rows)
            objects_dict = {'errorCode': '00', 'errorMsg': '查询成功', 'data': {'params': ''}}
            xmlroot = xmldata.getroot()
            for station in xmlroot.findall("./station"):
                station_dict = collections.OrderedDict()
                station_dict['common_site_name'] = station.get('common_site_name')
                site_list = []
                for site in station.findall("./site"):
                    site_dict = collections.OrderedDict()
                    site_dict['enbid'] = site.get('enbid')
                    site_dict['site_id'] = site.get('site_id')
                    site_dict['county'] = site.get('county')
                    site_dict['city'] = site.get('city')
                    site_dict['site_name'] = site.get('site_name')
                    site_list.append(site_dict)
                    sector_list = []
                    for sector in site.findall("./sector"):
                        sector_dict = collections.OrderedDict()
                        sector_dict['sector_id'] = sector.get('sector_id')
                        sector_list.append(sector_dict)
                        cell_list = []
                        for cell in sector.findall("./cell"):
                            cell_dict = collections.OrderedDict()
                            cell_dict['cell_name'] = cell.get('cell_name')
                            cell_dict['eci'] = cell.get('eci')
                            cell_dict['local_cell_id'] = cell.get('local_cell_id')
                            cell_dict['physical_cell_marker'] = cell.get('physical_cell_marker')
                            cell_dict['tac'] = cell.get('tac')
                            cell_dict['longitude'] = cell.get('longitude')
                            cell_dict['latitude'] = cell.get('latitude')
                            cell_dict['frequency_band'] = cell.get('frequency_band')
                            cell_dict['frequency_point'] = cell.get('frequency_point')
                            cell_dict['bandwidth'] = cell.get('bandwidth')
                            cell_dict['site_type'] = cell.get('site_type')
                            cell_dict['azimuth'] = cell.get('azimuth')
                            cell_dict['station_height'] = cell.get('station_height')
                            cell_dict['total_pitch_angle'] = cell.get('total_pitch_angle')
                            cell_list.append(cell_dict)
                        sector_dict['cell_arr'] = cell_list
                    site_dict['sector_arr'] = sector_list
                station_dict['site_arr'] = site_list
            objects_dict['data']['params'] = station_dict
        else:
            objects_dict['data']['params'] = None  # 如果没数据 返回null
        j = json.dumps(objects_dict, ensure_ascii=False, cls=DecimalEncoder)  # ensure_ascii=False解决中文问题
    except connection.Error as e:
        print(e)
        objects_dict = {'errorCode': '01', 'errorMsg': '{0}'}.__format__(e)
        j = json.dumps(objects_dict, ensure_ascii=False)  # ensure_ascii=False解决中文问题
    return j


# 用于更新工参数据，并记录更新log
def update_del_commsite(data,user):
    cursor = connection.cursor()
    temp_update_sql = '''
    UPDATE CELL_INFO_TDD_FDD SET {} WHERE ECI = '{}'
    '''
    temp_insert_sql = '''
    INSERT INTO CELL_INFO_TDD_FDD_LOG VALUES('{}','{}','{}','{}','{}');
    '''
    try:
        for d in data:
            d_eci = d['ECI']
            update_sql_sub = ''
            for k,v in d.items():
                update_sql_sub += "{}='{}',".format(k, v)
            info = str(d).replace("'",'"')
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            update_sql = temp_update_sql.format(update_sql_sub[:-1],d_eci)
            insert_sql = temp_insert_sql.format(d_eci,'update', info, user, now_time)
            cursor.execute(update_sql)
            cursor.execute(insert_sql)
            transaction.commit()
        return 'success'
    except:
        transaction.rollback()
        return 'fail'

# 用于更新工参数据，并记录更新log
def delete_del_commsite(data,user):
    cursor = connection.cursor()
    temp_delete_sql = '''
    DELETE FROM CELL_INFO_TDD_FDD WHERE ECI = '{}'
    '''
    temp_insert_sql1 = '''
    INSERT INTO CELL_INFO_TDD_FDD_BAK SELECT * FROM CELL_INFO_TDD_FDD WHERE ECI = '{}';
    '''
    temp_insert_sql2 = '''
        INSERT INTO CELL_INFO_TDD_FDD_LOG VALUES('{}','{}','{}','{}','{}');
        '''
    get_comm_site = '''
    SELECT 
    '''
    try:
        for d in data:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            # d_eci = d['ECI']
            delete_sql = temp_delete_sql.format(d)
            print(delete_sql)
            insert_sql1 = temp_insert_sql1.format(d)
            insert_sql2 = temp_insert_sql2.format(d,'delete','',user,now_time)
            cursor.execute(insert_sql1)
            cursor.execute(insert_sql2)
            cursor.execute(delete_sql)
            transaction.commit()
        return 'success'
    except:
        transaction.rollback()
        return 'fail'