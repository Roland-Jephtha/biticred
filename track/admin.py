from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Shipment)
admin.site.register(Contact)
admin.site.register(Phone)



admin.site.site_header = "Metro Express Parcel Service"
admin.site.index_title = "Manage Metro Express Parcel Service"
