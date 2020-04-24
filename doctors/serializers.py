from rest_framework import serializers
from users.serializers import UsersSerializer
from .models import Doctor

class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)
    description = serializers.CharField()


class DoctorSerializer(serializers.ModelSerializer):
    user = UsersSerializer()

    class Meta:
        model = Doctor
        fields = ('user',)
