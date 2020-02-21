# coding:utf-8

import xml.etree.cElementTree as ET

# 获取xml
class Data_to_xml:

    def __init__(self):
        self.b_root = ET.fromstring('<params ></params>')

    def getxml(self, results):
        for i in results:
            if not self.b_root.find("./station[@common_site_name='{}']".format(i[0])):
                elem = self.get_element('station', i)
                self.b_root.append(elem)
            elif not self.b_root.find("./station[@common_site_name='{}']/site[@site_name='{}']".format(i[0], i[5])):
                elem = self.get_element('site', i)
                self.b_root.find("./station[@common_site_name='{}']".format(i[0])).append(elem)
            elif not self.b_root.find("./station[@common_site_name='{}']/site[@site_name='{}']/sector[@sector_id='{}']".format(i[0], i[5], i[6])):
                elem = self.get_element('sector', i)
                self.b_root.find("./station[@common_site_name='{}']/site[@site_name='{}']".format(i[0], i[5])).append(elem)
            elif not self.b_root.find("./station[@common_site_name='{}']/site[@site_name='{}']/sector[@sector_id='{}']/cell[@cell_name='{}']".format(i[0], i[5], i[6], i[7])):
                elem = self.get_element('cell', i)
                self.b_root.find("./station[@common_site_name='{}']/site[@site_name='{}']/sector[@sector_id='{}']".format(i[0], i[5], i[6])).append(elem)
        self.pretty_xml(self.b_root, '\t', '\n')
        self.b_tree = ET.ElementTree(self.b_root)
        # self.b_tree.write('temp.xml', "UTF-8")
        return self.b_tree

    def pretty_xml(self, element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
        if element:  # 判断element是否有子元素
            if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
                element.text = newline + indent * (level + 1)
            else:
                element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
                # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
                # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
        temp = list(element)  # 将element转成list
        for subelement in temp:
            if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
                subelement.tail = newline + indent * (level + 1)
            else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
                subelement.tail = newline + indent * level
            self.pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


    def get_element(self, tag_type, datas):
        if tag_type == 'station':
            elem = ET.Element('station', {
                'common_site_name': datas[0],
                })
            site = ET.Element('site', {
                'enbid': datas[1],
                'site_id': datas[2],
                'county': datas[3],
                'city': datas[4],
                'site_name': datas[5],
                })
            elem.append(site)
            sector = ET.Element('sector', {
                'sector_id': datas[6],
                })
            site.append(sector)
            cell = ET.Element('cell', {
                'cell_name': datas[7],
                'eci': datas[8],
                'local_cell_id': datas[9],
                'physical_cell_marker': datas[10],
                'tac': datas[11],
                'longitude': datas[12],
                'latitude': datas[13],
                'frequency_band': datas[14],
                'frequency_point': datas[15],
                'bandwidth': datas[16],
                'site_type': datas[17],
                'azimuth': datas[18],
                'station_height': datas[19],
                'total_pitch_angle': datas[20],
                })
            sector.append(cell)
            return elem
        elif tag_type == 'site':
            elem = ET.Element('site', {
                'enbid': datas[1],
                'site_id': datas[2],
                'county': datas[3],
                'city': datas[4],
                'site_name': datas[5],
                })
            sector = ET.Element('sector', {
                'sector_id': datas[6],
                })
            elem.append(sector)
            cell = ET.Element('cell', {
                'cell_name': datas[7],
                'eci': datas[8],
                'local_cell_id': datas[9],
                'physical_cell_marker': datas[10],
                'tac': datas[11],
                'longitude': datas[12],
                'latitude': datas[13],
                'frequency_band': datas[14],
                'frequency_point': datas[15],
                'bandwidth': datas[16],
                'site_type': datas[17],
                'azimuth': datas[18],
                'station_height': datas[19],
                'total_pitch_angle': datas[20],
                })
            sector.append(cell)
            return elem
        elif tag_type == 'sector':
            elem = ET.Element('sector', {
                'sector_id': datas[6],
                })
            cell = ET.Element('cell', {
                'cell_name': datas[7],
                'eci': datas[8],
                'local_cell_id': datas[9],
                'physical_cell_marker': datas[10],
                'tac': datas[11],
                'longitude': datas[12],
                'latitude': datas[13],
                'frequency_band': datas[14],
                'frequency_point': datas[15],
                'bandwidth': datas[16],
                'site_type': datas[17],
                'azimuth': datas[18],
                'station_height': datas[19],
                'total_pitch_angle': datas[20],
                })
            elem.append(cell)
            return elem
        elif tag_type == 'cell':
            elem = ET.Element('cell', {
                'cell_name': datas[7],
                'eci': datas[8],
                'local_cell_id': datas[9],
                'physical_cell_marker': datas[10],
                'tac': datas[11],
                'longitude': datas[12],
                'latitude': datas[13],
                'frequency_band': datas[14],
                'frequency_point': datas[15],
                'bandwidth': datas[16],
                'site_type': datas[17],
                'azimuth': datas[18],
                'station_height': datas[19],
                'total_pitch_angle': datas[20],
                })
            return elem