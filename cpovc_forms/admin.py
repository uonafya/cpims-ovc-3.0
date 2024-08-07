from django.contrib import admin
from .models import (
    OVCCareQuestions, OVCCareForms, OVCCareTransfer, OVCProgramRegistration,
    OVCHIVManagement)


# Register your models here.
class OVCCareFormsInline(admin.TabularInline):
    model = OVCCareQuestions


class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_void',
                    'timestamp_created', 'timestamp_updated')
    search_fields = ('name',)
    inlines = [
        OVCCareFormsInline
    ]


admin.site.register(OVCCareForms, FormAdmin)


class OVCCareTransferAdmin(admin.ModelAdmin):
    list_display = ('person', 'reason',
                    'timestamp_created', 'timestamp_updated')
    search_fields = ('person__first_name', 'person__surname')


admin.site.register(OVCCareTransfer, OVCCareTransferAdmin)


class OVCCareQuestionsAdmin(admin.ModelAdmin):
    list_display = ('domain', 'code', 'question')

    search_fields = ('code', 'question', )


admin.site.register(OVCCareQuestions, OVCCareQuestionsAdmin)


class OVCProgramRegistrationAdmin(admin.ModelAdmin):
    list_display = ('program', 'person', 'child_cbo', 'child_chv')

    search_fields = ('person__first_name', 'person__surname',
                     'child_cbo__org_unit_name', )


admin.site.register(OVCProgramRegistration, OVCProgramRegistrationAdmin)


class OVCHIVManagementAdmin(admin.ModelAdmin):
    list_display = ('person', 'substitution_firstline_arv',
                    'hiv_confirmed_date', 'treatment_initiated_date', 'muac',
                    'muac_score', 'timestamp_created')

    search_fields = ('person__first_name', 'person__surname')

    list_filter = ['timestamp_created']


admin.site.register(OVCHIVManagement, OVCHIVManagementAdmin)
