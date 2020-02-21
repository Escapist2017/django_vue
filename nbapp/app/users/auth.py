# coding:utf-8
from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.libs.base_render import render_to_response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required

# 登陆
class Login(View):

    TEMPLATE = '/user/login.html'

    def get(self, request):

        next = request.GET.get('next', '')
        data = {'error': '', 'next': next}

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        exists = User.objects.filter(username=username).exists()
        user = authenticate(username=username, password=password)

        next = request.GET.get('next', '')

        data = {}

        # 判断账号密码问题
        if not username:
            data['error'] = '请填写账号'
        elif not password:
            data.update({'error':'请填写密码'})
        elif not exists:
            data.update({'error': '帐号不存在'})
        elif not user:
            data.update({'error': '密码错误'})

        # 如果有问题则重新加载
        if data:
            return render_to_response(request, self.TEMPLATE, data)

        # 如果没问题跳转首页
        login(request, user)

        if next:
            return redirect(next)

        return redirect(reverse('home'))

# 注册
class Regist(View):

    TEMPLATE = '/user/regist.html'

    def get(self, request):
        # if request.user.is_authenticated:
        #     return redirect(reverse('login'))
        return render_to_response(request, self.TEMPLATE)

    def post(self, request):

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_password = request.POST.get('check_password')
        exists = User.objects.filter(username=username).exists()
        data = {}

        # 判断账号密码问题
        if not username:
            data['error'] = '请填写账号'
        elif exists:
            data.update({'error': '帐号已存在'})
        elif not password or not check_password:
            data.update({'error': '请填写密码'})
        elif password != check_password:
            data.update({'error': '密码不一致'})

        # 如果有问题则重新加载
        if data:
            return render_to_response(request, self.TEMPLATE, data=data)

        # 如果没问题创建用户
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        data.update({'error':'注册成功'})
        return render_to_response(request, self.TEMPLATE, data=data)

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))

