from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('locations/city/api/', views.CityView.as_view(), name='city-api'),
]