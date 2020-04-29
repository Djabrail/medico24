from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('', views.ClinicListView.as_view(), name='list'),
    path('<slug:clinic_slug>/', views.ClinicTopListView.as_view(), name='top-list'),
    # path('api/', views.ClinicView.as_view(), name='api'),
]