from django.views.generic import View
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from .models import Clinic, ClinicService, ClinicType
from locations.models import City
from .serializers import ClinicSerializer

class ClinicListView(View):
    template_name = "clinics/list.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        clinics = Clinic.objects.filter(city=city)
        paginator = Paginator(clinics, 25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        context = {
            'clinics': clinics,
            'page_obj': page_obj,
            'city': city
        }

        return render(request, self.template_name, context)


class ClinicItemView(View):
    template_name = "clinics/item.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        clinic = get_object_or_404(Clinic, slug=kwargs['clinic_slug'], city_id=city)


        context = {
            'clinic': clinic,
            'city': city
        }

        return render(request, self.template_name, context)


class ClinicTypeItemView(View):
    template_name = "type/item.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        type = get_object_or_404(ClinicType, slug=kwargs['type_slug'])
        clinics = Clinic.objects.filter(city=city, type=type)

        context = {
            'clinics': clinics,
            'type': type,
            'city': city
        }

        return render(request, self.template_name, context)



class ClinicServiceListView(View):
    template_name = "service/list.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        clinics = Clinic.objects.filter(city=city)

        context = {
            'clinics': clinics,
            'city': city
        }

        return render(request, self.template_name, context)


class ClinicServiceItemView(View):
    template_name = "service/item.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])
        service = get_object_or_404(ClinicService, slug=kwargs['service_slug'])
        clinics = Clinic.objects.filter(city=city, service=service)

        context = {
            'clinics': clinics,
            'service': service,
            'city':city
        }

        return render(request, self.template_name, context)


class ClinicView(APIView):
    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response({"clinics": serializer.data})