from django.contrib import admin
from .models import (
    OVCCareQuestions, OVCCareForms, OVCCareTransfer, OVCCareQuestions)


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
    search_fields = ('person',)


admin.site.register(OVCCareTransfer, OVCCareTransferAdmin)


class OVCCareQuestionsAdmin(admin.ModelAdmin):
    list_display = ('domain', 'code', 'question')

    search_fields = ('code', 'question', )


admin.site.register(OVCCareQuestions, OVCCareQuestionsAdmin)
