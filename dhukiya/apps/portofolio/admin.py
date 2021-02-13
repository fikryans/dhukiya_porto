from django.contrib import admin
from .models import *


class PortofolioAdmin(admin.ModelAdmin):
    list_display = ('title','project_date','created_date','created_by')
    actions = None
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
admin.site.register(Portofolio, PortofolioAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

admin.site.register(Category, CategoryAdmin)

            
