from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "created_at")
    search_fields = ("name", "phone", "service")
    list_filter = ("service", "created_at")

    readonly_fields = (
        "name",
        "phone",
        "address",
        "service",
        "message",
        "created_at",
    )

    def has_add_permission(self, request):
        return False  # prevent manual creation

    def has_change_permission(self, request, obj=None):
        return False  # prevent editing

    def has_delete_permission(self, request, obj=None):
        return False  # optional: prevent deletion
