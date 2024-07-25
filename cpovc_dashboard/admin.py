from django.contrib import admin
from .models import IPInfo, COPTarget


class IPInfoAdmin(admin.ModelAdmin):
    list_display = ('agency', 'org_unit_id', 'org_unit',
                    'parent_unit', 'fyear')
    search_fields = ('parent_unit__org_unit_name', 'org_unit__org_unit_name')

    list_filter = ['fyear', 'parent_unit__org_unit_name', 'is_void']


admin.site.register(IPInfo, IPInfoAdmin)


class COPTargetAdmin(admin.ModelAdmin):
    list_display = ('agency_id', 'mechanism', 'hiv_burden', 'fyear', 'is_void')
    search_fields = ('mechanism__org_unit_name', 'agency_id')

    list_filter = ['fyear', 'agency', 'hiv_burden', 'is_void']


admin.site.register(COPTarget, COPTargetAdmin)
