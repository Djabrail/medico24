from django.contrib import admin
from .models import Service, Doctor, Diplom, Work, Education,Rank
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(Doctor)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Diplom)
admin.site.register(Rank)