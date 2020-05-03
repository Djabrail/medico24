from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('find/', views.SearchView.as_view(), name='search'),
    path('api/', views.SearchAPIView.as_view(), name='api'),
    # path('<slug:slug>/', views.CityView.as_view(), name='city'),
    path('cookie/city/', views.cookie_city, name='cookie-city'),
    path('<slug:city_slug>/', views.HomeCityView.as_view(), name='home-city'),
    path('<slug:city_slug>/<slug:service_slug>/', views.DoctorListView.as_view(), name='doctor-list'),
]