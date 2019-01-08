# !/usr/bin/python
# coding=utf-8
import re
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.messages.storage import session
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from x_admin.models import UserAdmin, Vipadmin
from django.views.decorators.csrf import csrf_exempt
from x_admin.funtion import get_hash
from django.contrib.auth import authenticate
@csrf_exempt
def page_not_found(request):
    return render(request,'404.html')

class Index(View):
    """"""
    def get(self,request):
       return render(request,'index.html')

class Viplist(View):
    def get(self,request):
        vipadmin = Vipadmin.objects.all()
        return render(request,"viplist.html",locals())
#编辑
class Vipedit(View):
    def get(self,request):
        edit_id = request.GET.get('id')
        eid = Vipadmin.objects.get(id=edit_id)
        return render(request,'vipedit.html',locals())
    def post(self, request):
        edit_id = request.POST.get('id')
        edit_name = request.POST.get('vipname')
        #添加数据
        editname=Vipadmin.objects.create(id=edit_id,vipname=edit_name)
        #更新数据信息
        # editvip = Vipadmin.objects.filter(id=edit_id).update(id=edit_id,vipname=edit_name)
        return redirect(reverse('user:viplist'),locals())

#删除
class Vipdel(View):
    def get(self,request):
        edit_id = request.GET.get('id') #herf 动态传参，获取到值
        Vipadmin.objects.filter(id=edit_id).delete()
        return redirect(reverse('user:viplist'))



class Adminlist(View):
    def get(self,request):
         adminlist= UserAdmin.objects.all()
         return render(request,"adminlist.html",locals())


#添加管理员
class Adminadd(View):
    def get(self,request):
        return render(request,'adminadd.html')
    def post(self,request):
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        is_superuser = request.POST.get('is_superuser')
        user = UserAdmin.objects.create(name=name,email=email,phone=phone,is_superuser=is_superuser)
        return redirect(reverse('user:adminlist'), locals())
#编辑管理员
class Adminedit(View):
    def get(self,request):
        edit_id = request.GET.get('id')  #获取到id
        edit = UserAdmin.objects.get(id=edit_id)
        return render(request,'adminedit.html',locals())
    def post(self,request):
        edit_id = request.GET.get('id')#获取到get提交的id,根据id进行编辑，更新。
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        is_superuser = request.POST.get('is_superuser')
        create_time = request.POST.get('create_time')
        editadmin = UserAdmin.objects.filter(id=edit_id).update(id=edit_id,name=name,email=email,phone=phone,is_superuser=is_superuser,create_time=create_time)
        return redirect(reverse('user:adminlist'), locals())


class Admindel(View):
    def get(self,request):
        admin_id = request.GET.get('id')
        useradmin = UserAdmin.objects.get(id=admin_id).delete()
        return redirect(reverse('user:adminlist'), locals())



class Login(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self, request):
        '''进行登录校验'''
        # 接受数据
        name = request.POST.get('name')
        password = request.POST.get('password')
        # a=get_hash(password)
        # print a
        if not all([name,password]):
            return render(request,'login.html',{'errmsg':'用户名或密码不能为空'})
        try:
            user = UserAdmin.objects.get(name=name)
        except UserAdmin.DoesNotExist:
            user = None
        if user:
            if get_hash(password)==user.password:
                return render(request, 'index.html', locals())
            else:
                return render(request, 'login.html', {'errmsg': '用户名或密码不正确'})
        else:
            return render(request, 'login.html', {'errmsg': '用户名或密码不正确'})



class Logout(View):
    """注销"""
    def get(self, request):
        request.session.clear()
        return redirect(reverse("user:login"))




