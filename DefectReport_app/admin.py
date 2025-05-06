from django.contrib import admin
from DefectReport_app.models import DefectStatus

class DefectStatusAdmin(admin.ModelAdmin):
    list_display = ('month', 'date', 'floor', 'line', 'qc_name', 'qc_id', 'supervisor_name')

admin.site.register(DefectStatus, DefectStatusAdmin)
