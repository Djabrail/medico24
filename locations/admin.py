from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(City, CityAdmin)