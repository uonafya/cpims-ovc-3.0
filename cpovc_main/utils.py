"""Common admin functions."""
from django.contrib import messages


def void_records(modeladmin, request, queryset):
    """
    These takes the queryset and sets the records value

    for is_void to True
    """
    queryset.update(is_void=True)
    message = ('Records Successfully voided (Soft delete).')
    messages.info(request, message)


void_records.short_description = "Void Records"
