from django.contrib import admin
from .models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_operator:
            return False
        return super().has_delete_permission(request, obj)