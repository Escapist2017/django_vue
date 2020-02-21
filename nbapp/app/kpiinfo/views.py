# coding:utf-8
from django.views.generic import View
from app.libs.base_render import render_to_response

class KpiinfoPage(View):

    TEMPLATE = '/kpiinfo/kpiinfo_page.html'

    # @method_decorator(login_required)
    def get(self, request):

        return render_to_response(request, self.TEMPLATE)

