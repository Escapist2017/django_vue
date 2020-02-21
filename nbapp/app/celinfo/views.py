# coding:utf-8
from django.views.generic import View
import json
from django.http import HttpResponse
from app.libs.base_render import render_to_response
from app.celinfo.base_Info import infos, funcs
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


class CelinfoPage(View):

    TEMPLATE = '/celinfo/celinfo_page.html'

    @method_decorator(login_required) # next=xxx
    def get(self, request):

        return render_to_response(request, self.TEMPLATE)

class Cel_Type(View):

    def get(self,request):
        v_type = request.GET.get('type')
        v_value = request.GET.get('value')
        if v_type in infos.Cellinfo_Type:
            sql = infos.CelName_sql.format(v_type, v_value)
            header = ('value',)
            j = funcs.response_del(sql, header)
            return HttpResponse(j)

class Cel_Info(View):

    def get(self, request):
        v_type = request.GET.get('type')
        v_value = request.GET.get('value')
        if v_type in infos.Cellinfo_Type: # 小区基本信息查询
            sql = infos.Cellinfo_sql.format(v_type, v_value)
            header = infos.Cellinfo_Header
            j = funcs.response_del(sql, header)
            return HttpResponse(j)

class Comm_Site(View):

    def get(self, request):
        v_type = request.GET.get('type') # celtype
        v_value = request.GET.get('value')
        if v_type in infos.Cellinfo_Type:  # 小区基本信息查询
            sql = infos.Comm_site_sql.format(v_type, v_value)
            j = funcs.response_del_commsite(sql)
            return HttpResponse(j)

class Comm_Site_update(View):

    def post(self, request):
        # v_type = request.POST.get('type') # update or delete
        v_param = request.POST.get('params')
        print(v_param)
        v_j = json.loads(v_param)
        v_type = v_j['type']
        v_data = v_j['data']
        user = request.user
        if v_type == 'update':
            v_eci = v_data[0]['ECI']
            sql = infos.Comm_site_sql.format('ECI', v_eci)
            result = funcs.update_del_commsite(v_data,user)
            if result=='success':
                j_str = funcs.response_del_commsite(sql)
                j_dict = json.loads(j_str)
                j_dict.update({'errorCode':'10','errorMsg':'更新成功'})
                j = json.dumps(j_dict)
                return HttpResponse(j)
            objects_dict = {'errorCode': '11', 'errorMsg': '更新失败'}
            j = json.dumps(objects_dict, ensure_ascii=False)
            return HttpResponse(j)
        elif v_type == 'delete':
            v_eci = v_data[0]
            sql = infos.Comm_site_sql.format('ECI', v_eci)
            j_str = funcs.response_del_commsite(sql)
            j_dict = json.loads(j_str)
            j_dict.update({'errorCode': '20', 'errorMsg': '删除成功'})
            j = json.dumps(j_dict)
            result = funcs.delete_del_commsite(v_data,user)
            if result == 'success':
                return HttpResponse(j)
            objects_dict = {'errorCode': '21', 'errorMsg': '删除失败'}
            j = json.dumps(objects_dict, ensure_ascii=False)
            return HttpResponse(j)
