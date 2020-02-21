# coding:utf-8

# 模糊查询的配置信息

CelName_Header = ()

CelName_sql = '''
SELECT {0} FROM CELL_INFO_TDD_FDD where {0} like '%{1}%' GROUP BY {0} limit 20 
'''

# 小区信息查询的配置信息

Cellinfo_Header = (
    'ECI','地市','区县','站名','小区名','站号','eNBID','本地小区ID','物理小区标识','跟踪区','经度'
    ,'纬度','频段','频点号','带宽','站型','方位角','站高','总俯仰角','内置下倾角'
    ,'电下倾角','机械下倾角','厂家','omc是否存在','覆盖半径','半功率角','备注'
    ,'室分及拉远覆盖区域','室分及拉远信源BBU','网格信息','类型','是否共址','共址eNB'
    ,'共址站名','共站名','共站扇区','FDD及DF共站扇区总数','共站备注','SECTOR','POINTS'
)

Cellinfo_Type = ('ECI','站名','小区名','站号','eNBID','共站名')

Cellinfo_sql = '''
SELECT `ECI`,`地市`,`区县`,`站名`,`小区名`,`站号`,`eNBID`,`本地小区ID`,`物理小区标识`,`跟踪区`,`经度`
,`纬度`,`频段`,`频点号`,`带宽`,`站型`,`方位角`,`站高`,`总俯仰角`,`内置下倾角`,`电下倾角`,`机械下倾角`
,`厂家`,`omc是否存在`,`覆盖半径`,`半功率角`,`备注`,`室分及拉远覆盖区域`,`室分及拉远信源BBU`,`网格信息`
,`类型`,`是否共址`,`共址eNB`,`共址站名`,`共站名`,`共站扇区`,`FDD及DF共站扇区总数`,`共站备注`,SECTOR,POINTS
FROM CELL_INFO_TDD_FDD T WHERE `{}` = '{}'
'''

# 共站信息查询的配置信息
Comm_site_dict = {
'共站名':'common_site_name',
'eNBID':'enbid',
'站号':'site_id',
'区县':'county',
'地市':'city',
'站名':'site_name',
'SECTOR':'sector_id',
'小区名':'cell_name',
'ECI':'eci',
'本地小区ID':'local_cell_id',
'物理小区标识':'physical_cell_marker',
'跟踪区':'tac',
'经度':'longitude',
'纬度':'latitude',
'频段':'frequency_band',
'频点号':'frequency_point',
'带宽':'bandwidth',
'站型':'site_type',
'方位角':'azimuth',
'站高':'station_height',
'总俯仰角':'total_pitch_angle',
}

Comm_site_dict_2 = {
'common_site_name':'共站名',
'enbid':'eNBID',
'site_id':'站号',
'county':'区县',
'city':'地市',
'site_name':'站名',
'sector_id':'SECTOR',
'cell_name':'小区名',
'eci':'ECI',
'local_cell_id':'本地小区ID',
'physical_cell_marker':'物理小区标识',
'tac':'跟踪区',
'longitude':'经度',
'latitude':'纬度',
'frequency_band':'频段',
'frequency_point':'频点号',
'bandwidth':'带宽',
'site_type':'站型',
'azimuth':'方位角',
'station_height':'站高',
'total_pitch_angle':'总俯仰角',
}

Comm_site_sql = '''
SELECT `共站名`,`eNBID`,`站号`,`区县`,`地市`,`站名`,`SECTOR`,`小区名`,`ECI`,`本地小区ID`,`物理小区标识`,`跟踪区`,`经度`,`纬度`,`频段`,`频点号`,`带宽`,`站型`,`方位角`,`站高`,`总俯仰角`
FROM CELL_INFO_TDD_FDD T WHERE `共站名` <> '无' AND `共站名` = (SELECT `共站名` FROM CELL_INFO_TDD_FDD WHERE `{}`='{}' LIMIT 1)
'''

# update request data
'''
{"type":"update",
"data":[{"ECI":"120040897",
"物理小区标识":"292",
"跟踪区":"26590",
"经度":"121.534521",
"纬度":"29.876587",
"频段":"D7",
"频点号":"41140",
"带宽":"20",
"站型":"宏站",
"方位角":"70",
"站高":"19",
"总俯仰角":"8"
},
{"ECI":"120040898",
"物理小区标识":"348",
"跟踪区":"26590",
"经度":"121.534521",
"纬度":"29.876587",
"频段":"D7",
"频点号":"41140",
"带宽":"20",
"站型":"宏站",
"方位角":"140",
"站高":"23",
"总俯仰角":"8"
}]}
'''

# delete request data

'''
{
"type":"delete",
"data":["53260993","53261249"]
}
'''
