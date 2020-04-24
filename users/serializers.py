from rest_framework import serializers

class UsersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=255)
    slug = serializers.CharField(max_length=255)