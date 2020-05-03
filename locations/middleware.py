from django.shortcuts import render, get_object_or_404
from  .models import City

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        city_slug = view_kwargs.get('city_slug', None)
        if city_slug:
            city = get_object_or_404(City, slug=city_slug)
            print(city)
            request.session['city_id'] = city.id
            request.session['city_slug'] = city.slug
            request.session['city_name'] = city.name