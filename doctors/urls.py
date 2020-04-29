from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='list'),
    path('<slug:doctor_slug>/', views.DoctorItemView.as_view(), name='item'),
]