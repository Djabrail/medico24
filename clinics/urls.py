from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('<slug:city_slug>/clinici/', views.ClinicListView.as_view(), name='list'),
    path('<slug:city_slug>/clinici/<slug:clinic_slug>/', views.ClinicItemView.as_view(), name='item'),
    path('<slug:city_slug>/top/<slug:type_slug>/', views.ClinicTypeItemView.as_view(), name='type-item'),
    path('<slug:city_slug>/uslugi/', views.ClinicServiceListView.as_view(), name='clinic-service-list'),
    path('<slug:city_slug>/uslugi/<slug:service_slug>/', views.ClinicServiceItemView.as_view(), name='clinic-service-item'),
    # path('api/', views.ClinicView.as_view(), name='api'),
]