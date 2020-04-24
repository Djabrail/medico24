from django.contrib import admin
from .models import Clinic, ClinicService, ClinicType


class ClinicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ClinicServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ClinicTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Clinic, ClinicAdmin)
admin.site.register(ClinicService, ClinicServiceAdmin)
admin.site.register(ClinicType, ClinicTypeAdmin)