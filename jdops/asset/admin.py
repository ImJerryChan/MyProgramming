# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Host,
)
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'status', 'update_time', 'created_time')


admin.site.register(Host, HostAdmin)
