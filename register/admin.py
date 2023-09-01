from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

UM = get_user_model()


class UMAdmin(UserAdmin):
    model = UM
    list_display = ["id", "email", "is_admin"]
    fieldsets = [["Edit User Account", {"fields": ["email", "password"]}]]
    add_fieldsets = [["Create User Account", {"fields": ["email", "password1", "password2"]}]]
    filter_horizontal = []
    list_filter = []
    ordering = ("email",)



admin.site.register(UM, UMAdmin)
