from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.


admin.site.register(Shipment)
admin.site.register(Contact)
admin.site.register(Phone)
admin.site.unregister(Group)


admin.site.site_header = "BitiCred Speed Logistics"
admin.site.index_title = "Manage BitiCred Speed Logistics"
