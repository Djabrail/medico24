from django import template
from locations.models import City

register = template.Library()


@register.simple_tag
def locations_city():
    return City.objects.get(id=3)