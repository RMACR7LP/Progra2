# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from usuario.models import Texto

class Textoadmin(admin.ModelAdmin):
    pass

admin.site.register(Texto,Textoadmin)
