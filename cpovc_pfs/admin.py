from django.contrib import admin
from .models import OVCPreventiveRegistration
from cpovc_pfs.pmtct.models import OVCPMTCTRegistration


class OVCPreventiveRegistrationAdmin(admin.ModelAdmin):
    """PMTCT Registration."""

    search_fields = ['person']
    list_display = ['registration_date', 'person', 'is_void', ]

    readonly_fields = ['person']
    list_filter = ['is_void']


admin.site.register(OVCPreventiveRegistration, OVCPreventiveRegistrationAdmin)


class OVCPMTCTRegistrationAdmin(admin.ModelAdmin):
    """PMTCT Registration."""

    search_fields = ['person']
    list_display = ['registration_date', 'person', 'is_void', ]

    readonly_fields = ['person']
    list_filter = ['is_void']


admin.site.register(OVCPMTCTRegistration, OVCPMTCTRegistrationAdmin)
