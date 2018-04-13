# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group as UserGroup
from django.db import models

class Host(models.Model):
    STATUS_ITEMS = (
        (1, "空闲"),
        (2, "使用中"),
        (3, "已报废"),
    )
    name = models.CharField(max_length=100, blank=True, verbose_name="主机名")
    ip = models.GenericIPAddressField(verbose_name="主机IP")
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name="主机状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name_plural = "主机"
