from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "name"
    )
    list_filter = (
        "email",
        "name"
    )
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "email",
                    "name",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            "User",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
