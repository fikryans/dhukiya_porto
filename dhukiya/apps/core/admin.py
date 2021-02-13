from django.contrib import admin
from .models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'last_update')
    def has_add_permission(self, request):
        count = Setting.objects.all().count()
        if count == 0:
            return True
        return False
admin.site.register(Setting, SettingAdmin)
