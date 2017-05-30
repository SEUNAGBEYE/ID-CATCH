# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from id_management.models import UserAccount, Address, Id

from django.contrib import admin

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Address)
admin.site.register(Id)
