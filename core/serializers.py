from rest_framework import serializers
from clinics.serializers import ClinicSerializer
from doctors.serializers import ServiceSerializer, DoctorSerializer

class SearchSerializers(serializers.Serializer):
    clinics = ClinicSerializer(many = True)
    services = ServiceSerializer(many = True)
    doctors = DoctorSerializer(many=True)
