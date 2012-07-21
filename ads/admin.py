#  -*- coding: UTF-8 -*-
from django.contrib import admin

from ads   import models
admin.site.register(models.Ad)
admin.site.register(models.AdUser)

__author__ = 'copyliu'
