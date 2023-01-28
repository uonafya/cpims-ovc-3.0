"""Admin backend for editing some admin details."""
from django.contrib import admin

from .models import (RegPerson, RegOrgUnit, RegOrgUnitsAuditTrail,
                     RegPersonsAuditTrail, RegPersonsTypes, OVCHouseHold)


from cpovc_auth.models import AppUser

from cpovc_main.utils import dump_to_csv


class PersonInline(admin.StackedInline):
    model = AppUser
    exclude = ('password', )


class RegPersonAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['first_name', 'surname', 'other_names']
    list_display = ['id', 'first_name', 'surname', 'date_of_birth',
                    'age', 'sex_id', 'is_void']
    # readonly_fields = ['id']
    list_filter = ['is_void', 'sex_id', 'created_at']

    inlines = (PersonInline, )


admin.site.register(RegPerson, RegPersonAdmin)


class RegPersonTypesAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['person__surname', 'person__first_name']
    list_display = ['id', 'person', 'person_type_id',
                    'date_created', 'is_void', ]

    def date_created(self, obj):
        return obj.person.created_at
    date_created.admin_order_field = 'date'
    date_created.short_description = 'Date Created'
    readonly_fields = ['person']
    list_filter = ['is_void', 'person_type_id', 'person__created_at']


admin.site.register(RegPersonsTypes, RegPersonTypesAdmin)


class RegOrgUnitAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['org_unit_name', 'org_unit_id_vis']
    list_display = ['id', 'org_unit_id_vis', 'org_unit_name',
                    'parent_org_unit_id', 'parent_unit', 'is_void']
    # readonly_fields = ['id']
    list_filter = ['is_void', 'org_unit_type_id', 'created_at',
                   'parent_org_unit_id']
    actions = [dump_to_csv]


admin.site.register(RegOrgUnit, RegOrgUnitAdmin)


class OrgUnitAuditAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['org_unit_id']
    list_display = ['transaction_id', 'transaction_type_id', 'ip_address',
                    'app_user_id', 'timestamp_modified']
    # readonly_fields = ['id']
    list_filter = ['transaction_type_id', 'app_user_id']


admin.site.register(RegOrgUnitsAuditTrail, OrgUnitAuditAdmin)


class PersonsAuditAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['person_id']
    list_display = ['transaction_id', 'transaction_type_id', 'ip_address',
                    'app_user_id', 'timestamp_modified']
    # readonly_fields = ['id']
    list_filter = ['transaction_type_id', 'app_user_id']


admin.site.register(RegPersonsAuditTrail, PersonsAuditAdmin)


class OVCHouseHoldAdmin(admin.ModelAdmin):
    """Register persons admin."""

    search_fields = ['index_child', 'members']
    list_display = ['index_child_id', 'index_child', 'members']
    # readonly_fields = ['id']
    list_filter = ['is_void']


admin.site.register(OVCHouseHold, OVCHouseHoldAdmin)
