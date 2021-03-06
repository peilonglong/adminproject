# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-05 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('x_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=20, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('phone', models.CharField(max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('email', models.CharField(max_length=20, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('is_superuser', models.BooleanField(default=0, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xaf\xe8\xb6\x85\xe7\xba\xa7\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')),
                ('create_time', models.DateTimeField(max_length=50, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('start', models.BooleanField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('vipadmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='x_admin.Vipadmin', verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe7\xad\x89\xe7\xba\xa7')),
            ],
        ),
        migrations.RemoveField(
            model_name='rule',
            name='role',
        ),
        migrations.RemoveField(
            model_name='rulegroup',
            name='role',
        ),
        migrations.RemoveField(
            model_name='rulegroup',
            name='rulegroup',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roleuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rulegroup',
        ),
        migrations.RemoveField(
            model_name='viplist',
            name='address',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.DeleteModel(
            name='Rulegroup',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Viplist',
        ),
    ]
