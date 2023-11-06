from django.contrib import admin
from .models import DeviceManagement


@admin.action(description="Mark selected devices as blacklisted")
def make_blacklisted(modeladmin, request, queryset):
    queryset.update(is_blocked=True)


@admin.action(description="Mark selected devices as activated")
def make_activated(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected devices as cleared for re-use")
def make_voided(modeladmin, request, queryset):
    queryset.update(is_void=True)


class DeviceManagementAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'get_user', 'user', 'get_person',
                    'get_names', 'timestamp_created', 'timestamp_updated',
                    'is_active', 'is_blocked', 'is_void')
    search_fields = ('device_id', 'timestamp_created', 'user__username')

    list_filter = ['is_active', 'is_blocked', 'is_void']

    @admin.display(ordering='user__username', description='User ID')
    def get_user(self, obj):
        return obj.user.id

    @admin.display(ordering='user__username', description='Person ID')
    def get_person(self, obj):
        return obj.user.reg_person_id

    @admin.display(ordering='user__reg_person_id', description='Person Names')
    def get_names(self, obj):
        names = '%s %s' % (
            obj.user.reg_person.first_name, obj.user.reg_person.surname)
        return names

    actions = ["delete_selected", make_blacklisted,
               make_activated, make_voided]


admin.site.register(DeviceManagement, DeviceManagementAdmin)
