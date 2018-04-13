# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.GenericIPAddressField(verbose_name='\u4e3b\u673aIP')),
                ('status', models.IntegerField(choices=[(1, '\u7a7a\u95f2'), (2, '\u4f7f\u7528\u4e2d'), (3, '\u5df2\u62a5\u5e9f')], default=1, verbose_name='\u4e3b\u673a\u72b6\u6001')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u4e3b\u673a',
            },
        ),
    ]