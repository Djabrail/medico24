from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:city_slug>/vrach/', include('doctors.urls', namespace='doctors')),
    path('<slug:city_slug>/clinici/', include('clinics.urls', namespace='clinics')),
    path('locations/', include('locations.urls', namespace='locations')),
    path('', include('core.urls', namespace='core')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)