from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from dashboard.models import MaintenanceModel, ConsumableModel
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'age')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username',)

# 追加したモデルを管理サイトに追加
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MaintenanceModel)
admin.site.register(ConsumableModel)
