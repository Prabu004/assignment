from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ['username', 'email', 'role', 'is_active', 'last_login']
    
    list_filter = ['role', 'is_active']
    
    search_fields = ['username', 'email', 'role']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    ordering = ['-date_joined']

admin.site.register(CustomUser, CustomUserAdmin)
