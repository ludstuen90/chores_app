# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Chore, Boyfriend, Clean

class CleanAdmin(admin.ModelAdmin):
    list_display = ('chore_completed', 'cleaner', 'time')

# Register your models here.
admin.site.register(Chore)
admin.site.register(Boyfriend)
admin.site.register(Clean, CleanAdmin)
