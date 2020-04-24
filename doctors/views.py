from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from clinics.models import Clinic
from locations.models import City
from .models import Doctor, Service


class DoctorListView(View):
    template_name = "doctor/list.html"

    def get(self, request, *args, **kwargs):
        context= {}
        city = get_object_or_404(City, slug=kwargs['city_slug'])
        doctors = Doctor.objects.filter(clinic__city=city.id)
        context = {
            "doctors" : doctors
        }

        return render(request, self.template_name, context)


class DoctorItemView(View):
    model = City
    template_name = "doctor/item.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        doctor = get_object_or_404(Doctor, user_id=kwargs['doctor_id'])
        service = Service.objects.filter(doctor=doctor)[:1]

        if city:
            request.session['city_id'] = city.id
            request.session['city_slug'] = city.slug
            request.session['city_name'] = city.name

        context = {
            "doctor" : doctor,
            "service": service
        }

        return render(request, self.template_name, context)