import json
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from itertools import chain
from users.models import User

from clinics.models import Clinic, ClinicService, ClinicType
from doctors.models import Service, Doctor
from locations.models import City

from .forms import SearchForm

from .serializers import SearchSerializers

from locations.location import Location

class HomeView(View):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        context= {}
        search_form = SearchForm()


        if "city_id" in request.session:
            location_city_id = request.session['city_id']
        else:
            location_city_id = request.session['city_id'] = 2
            request.session['city_slug'] = 'moskva'
            request.session['city_name'] = 'Москва'


        services = Service.objects.filter(doctor__clinic__city__id=location_city_id).distinct()[:4]
        clinic_type = ClinicType.objects.filter(clinic__city__id=location_city_id).distinct()[:4]
        clinic_service = ClinicService.objects.filter(clinic__city__id=location_city_id).distinct()[:4]

        context = {
            'search_form': search_form,
            'services': services,
            'clinic_type': clinic_type,
            'clinic_service': clinic_service
        }

        return render(request, self.template_name, context)


class SearchView(View):
    template_name = "core/search.html"

    def get(self, request, *args, **kwargs):
        context= {}
        search_form = SearchForm()

        q = request.GET.get('q')
        if q:
            query_sets = []

            if "city_id" in request.session:
                location_city_id = request.session['city_id']
            else:
                location_city_id = request.session['city_id'] = 2
                request.session['city_slug'] = 'moskva'
                request.session['city_name'] = 'Москва'

            doctor = Doctor.objects.filter(clinic__city__id=location_city_id)


            answer_clinics = Clinic.objects.filter(city=location_city_id, name__icontains=q.title())
            answer_services = Service.objects.filter(name__icontains=q.title())
            answer_doctors = doctor.filter(
                Q(user__first_name__icontains=q.title()) |
                Q(user__last_name__icontains=q.title()) |
                Q(user__patronymic__icontains=q.title()))
        context = {
            'search_form': search_form,
            "clinics" : answer_clinics,
            'services' : answer_services,
            'doctors': answer_doctors
        }

        return render(request, self.template_name, context)

class CityView(View):
    template_name = "core/city.html"

    def get(self, request, *args, **kwargs):
        context= {}


        clinics = Clinic.objects.filter(city__slug=kwargs['slug'])

        context = {
            "clinics" : clinics
        }

        return render(request, self.template_name, context)

class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        filters = {}

        if "city_id" in request.session:
            location_city_id = request.session['city_id']
        else:
            location_city_id = request.session['city_id'] = 2
            request.session['city_slug'] = 'moskva'
            request.session['city_name'] = 'Москва'


        clinics = Clinic.objects.filter(city=location_city_id)
        for clinic in clinics:
            print(clinic.city.id)
        doctors = Doctor.objects.filter(clinic__city=location_city_id).distinct()



        filters['clinics'] = clinics
        filters['services'] = Service.objects.all()
        filters['doctors'] = doctors
        serializer = SearchSerializers(filters)
        return Response (serializer.data, status=status.HTTP_200_OK)


def cookie_city(request):
    city_id = request.GET.get('city_id', None)
    city_slug = request.GET.get('city_slug', None)
    city_name = request.GET.get('city_name', None)

    city_id_session = request.session['city_id'] = city_id
    request.session['city_slug'] = city_slug
    request.session['city_name'] = city_name

    city = City.objects.get(id=city_id_session)

    data = {
        'city_slug': city.slug
    }
    return JsonResponse(data)


class DoctorListView(View):
    model = City
    template_name = "core/doctors.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])

        if city:
            request.session['city_id'] = city.id
            request.session['city_slug'] = city.slug
            request.session['city_name'] = city.name

        clinics = Clinic.objects.filter(city=city.id)
        services = get_object_or_404(Service, slug=kwargs['service_slug'])

        doctors = Doctor.objects.filter(clinic__in=clinics, service=services.id).distinct()
        doctors_count = doctors.count()

        context = {
            "doctors" : doctors,
            "service": services,
            "doctors_count": doctors_count
        }

        return render(request, self.template_name, context)


class ClinicServiceListView(View):
    template_name = "core/clinic-service-list.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])

        context = {
        }

        return render(request, self.template_name, context)