from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('<slug:city_slug>/vrach/', views.DoctorListView.as_view(), name='list'),
    path('<slug:city_slug>/vrach/<slug:doctor_slug>/', views.DoctorItemView.as_view(), name='item'),
]