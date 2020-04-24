from rest_framework import serializers

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)