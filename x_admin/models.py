# !/usr/bin/python
# coding=utf-8
from datetime import datetime
# Create your models here.
from django.db import models

#会员等级
class Vipadmin(models.Model):
    vipname = models.CharField(max_length=20,verbose_name='等级名称')

#用户表
class UserAdmin(models.Model):
    '''会员等级'''
    admin_super = (
        (0,'普通用户'),
        (1, '超级管理员'),
    )
    name = models.CharField(max_length=20, verbose_name='用户名',unique=True)
    password = models.CharField(max_length=120, verbose_name='密码')
    phone = models.CharField(max_length=16, verbose_name='联系电话')
    email = models.CharField(max_length=60,verbose_name='邮箱')
    is_superuser = models.SmallIntegerField(choices=admin_super,default=0,verbose_name='是否是超级管理员')
    create_time = models.DateField(max_length=50, verbose_name='创建时间')
    start = models.BooleanField(default=1, verbose_name='状态')
    vipadmin = models.ForeignKey('Vipadmin',verbose_name='关联等级',on_delete=models.CASCADE)







