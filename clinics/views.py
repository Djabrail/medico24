from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from .models import Clinic
from locations.models import City
from .serializers import ClinicSerializer

class ClinicListView(View):
    template_name = "clinics/list.html"

    def get(self, request, *args, **kwargs):
        context= {}


        context = {
        }

        return render(request, self.template_name, context)


class ClinicTopListView(View):
    template_name = "clinics/top-list.html"

    def get(self, request, *args, **kwargs):
        context= {}

        city = get_object_or_404(City, slug=kwargs['city_slug'])

        context = {
        }

        return render(request, self.template_name, context)

class ClinicView(APIView):
    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response({"clinics": serializer.data})