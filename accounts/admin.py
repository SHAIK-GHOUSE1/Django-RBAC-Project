from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "role",
        "email",
        "is_active",
        "date_joined",
    )  # Customize fields to display in the admin list view
    search_fields = (
        "username",
        "email",
        "role",
    )  # Fields that can be searched in the admin panel
    list_filter = ("role", "is_active")  # Allow filtering by 'role' and 'is_active'


admin.site.register(CustomUser, CustomUserAdmin)
