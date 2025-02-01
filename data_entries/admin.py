from django.contrib import admin
from .models import DataEntry

# Register your models here.
admin.site.register(DataEntry)
class DataEntryAdmin(admin.ModelAdmin):
    list_display = ('data', 'date', 'user')
    list_filter = ('date', 'user')
    search_fields = ('data', 'user')
    ordering = ('date',)
    filter_horizontal = ()
    date_hierarchy = 'date'
    readonly_fields = ('date', 'user')
    fieldsets = (
        (None, {'fields': ('data', 'date', 'user')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('data', 'date', 'user'),
        }),
    )
    def has_delete_permission(self, request, obj=None):
        if request.user.is_operator:
            return False
        return super().has_delete_permission(request, obj)