from django.contrib import admin
from .models import OVCPMTCTRegistration, OVCHEITracker


class OVCPMTCTRegistrationAdmin(admin.ModelAdmin):
    """PMTCT Registration."""

    search_fields = ['person__id']
    list_display = ['registration_date', 'person', 'is_void', ]

    readonly_fields = ['person']
    list_filter = ['is_void']


admin.site.register(OVCPMTCTRegistration, OVCPMTCTRegistrationAdmin)


class OVCHEITrackerAdmin(admin.ModelAdmin):
    """PMTCT Registration."""

    search_fields = ['person__id']
    list_display = ['date_of_event', 'person', 'is_void', ]

    readonly_fields = ['person']
    list_filter = ['is_void']


admin.site.register(OVCHEITracker, OVCHEITrackerAdmin)
