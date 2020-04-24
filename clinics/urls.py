from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('', views.ClinicListView.as_view(), name='list'),
    # path('ss/<slug:clinic_id>-<slug:clinic_slug>/', views.ClinicItemView.as_view(), name='list'),
    # path('api/', views.ClinicView.as_view(), name='api'),
]