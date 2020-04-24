from rest_framework import serializers

from locations.serializers import CitySerializer

class ClinicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    description = serializers.CharField()
    city = CitySerializer(many=True, read_only=True)