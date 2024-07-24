from django.contrib import admin

from .models import OVCEvent, OVCMobileEvent, CasePlanTemplateEvent


class OVCEventAdmin(admin.ModelAdmin):
    """Aggregate data admin."""

    search_fields = ['ovc_cpims_id', 'user_id']
    list_display = ['id', 'form_type', 'user_id',
                    'ovc_cpims_id', 'date_of_event']

    list_filter = ['form_type', 'date_of_event']


admin.site.register(OVCEvent, OVCEventAdmin)


class OVCMobileEventAdmin(admin.ModelAdmin):
    """Aggregate data admin."""

    search_fields = ['ovc_cpims_id', 'user_id']
    list_display = ['id', 'user_id', 'ovc_cpims_id', 'date_of_event']

    list_filter = ['date_of_event']


admin.site.register(OVCMobileEvent, OVCMobileEventAdmin)


class CasePlanTemplateEventAdmin(admin.ModelAdmin):
    """Aggregate data admin."""

    search_fields = ['ovc_cpims_id', 'user_id']
    list_display = ['id', 'user_id', 'ovc_cpims_id', 'date_of_event']

    list_filter = ['date_of_event']


admin.site.register(CasePlanTemplateEvent, CasePlanTemplateEventAdmin)

