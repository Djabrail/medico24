from rest_framework.response import Response
from rest_framework.views import APIView
from .models import City
from .serializers import CitySerializer

class CityView(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"cities": serializer.data})


