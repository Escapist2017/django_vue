
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import CellsLevel
from .filters import CellsFilter
from .serializers import CellsLevelSerializer, CellsInfoSerializer

class CellsPagination(PageNumberPagination):
    page_size = 10 # 每页显示的多少条记录
    page_size_query_param = 'page_size' # 前台控制每页显示多少条
    page_query_param = "p" # 前台查询第几页的参数
    max_page_size = 100 # 后台控制显示的最大记录条数，防止前台输入的查询条数过大

class CellsLevelViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    共站小区列表
    """
    queryset = CellsLevel.objects.filter(level_type=1)
    serializer_class = CellsLevelSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CellsFilter
    search_fields = ('name', 'sub_lev__name',
                     'sub_lev__sub_lev__sub_cells__cell_name',
                     'sub_lev__sub_lev__sub_cells__enbid',
                     'sub_lev__sub_lev__sub_cells__eci') # 耶 解决了 多级查询
    pagination_class = CellsPagination
