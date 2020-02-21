from datetime import datetime
from django.db import models

# Create your models here.


class CellsLevel(models.Model):
    """
    小区信息的多级分类
    """
    LEVEL_TYPE = (
        (1, "共站"),
        (2, "基站"),
        (3, "扇区")
    )

    name = models.CharField(default="", max_length=50, verbose_name="类别名", help_text="类别名")
    # 设置目录树的级别
    level_type = models.IntegerField(choices=LEVEL_TYPE, verbose_name="类目级别", help_text="类目级别")
    # 设置models有一个指向自己的外键
    parent_level = models.ForeignKey("self", on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name="父级别",
                                        help_text="父级别",related_name="sub_lev")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # unique_together = (("name", "code", "level_type", "parent_level"),)
        verbose_name = "共站分级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CellsInfo(models.Model):
    """
    工参信息
    """
    dist = models.CharField(default="", max_length=10, verbose_name="地市", help_text="地市")
    city = models.CharField(default="", max_length=10, verbose_name="区县", help_text="区县")
    site_name = models.CharField(default="", max_length=50, verbose_name="基站名", help_text="基站名")
    cell_name = models.CharField(default="", max_length=50, verbose_name="小区名", help_text="小区名")
    site_id = models.CharField(default="", max_length=20, verbose_name="站号", help_text="站号")
    enbid = models.CharField(default="", max_length=20, verbose_name="eNBID", help_text="eNBID")
    local_cell_id = models.CharField(default="", max_length=20, verbose_name="本地小区ID", help_text="本地小区ID")
    eci = models.CharField(default="", max_length=20, verbose_name="ECI", help_text="ECI")
    physical_cell_id = models.CharField(default="", max_length=20, verbose_name="物理小区标识", help_text="物理小区标识")
    pci_mod3 = models.CharField(default="", max_length=20, verbose_name="PCIMOD3", help_text="PCIMOD3")
    tac = models.CharField(default="", max_length=20, verbose_name="跟踪区", help_text="跟踪区")
    longitude = models.CharField(default="", max_length=20, verbose_name="经度", help_text="经度")
    latitude = models.CharField(default="", max_length=20, verbose_name="纬度", help_text="纬度")
    frequency_band = models.CharField(default="", max_length=20, verbose_name="频段", help_text="频段")
    frequency_point = models.CharField(default="", max_length=20, verbose_name="频点号", help_text="频点号")
    bandwidth = models.CharField(default="", max_length=20, verbose_name="带宽", help_text="带宽")
    site_type = models.CharField(default="", max_length=20, verbose_name="站型", help_text="站型")
    azimuth = models.CharField(default="", max_length=20, verbose_name="方位角", help_text="方位角")
    station_height = models.CharField(default="", max_length=20, verbose_name="站高", help_text="站高")
    total_pitch_angle = models.CharField(default="", max_length=20, verbose_name="总俯仰角", help_text="总俯仰角")
    inner_pitch_angle = models.CharField(default="", max_length=20, verbose_name="内置下倾角", help_text="内置下倾角")
    electronic_pitch_angle = models.CharField(default="", max_length=20, verbose_name="电下倾角", help_text="电下倾角")
    mechanical_pitch_angle = models.CharField(default="", max_length=20, verbose_name="机械下倾角", help_text="机械下倾角")
    sprod_name = models.CharField(default="", max_length=20, verbose_name="厂家", help_text="厂家")
    grid_info = models.CharField(default="", max_length=50, verbose_name="网格信息", help_text="网格信息")
    band_type = models.CharField(default="", max_length=20, verbose_name="类型", help_text="类型")
    common_site_name = models.CharField(default="", max_length=50, verbose_name="共站名", help_text="共站名")
    sector = models.CharField(default="", max_length=50, verbose_name="扇区", help_text="扇区")
    desc = models.TextField(default="", verbose_name="描述", help_text="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    parent_level= models.ForeignKey(CellsLevel, on_delete=models.CASCADE,
                                        null=True, blank=True, verbose_name="父级别",
                                        help_text="父级别",related_name="sub_cells")

    class Meta:
        verbose_name = "工参信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cell_name