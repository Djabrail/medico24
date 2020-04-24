

class Location(object):

    def __init__(self, request):

        location_city_id = request.session['city_id'] = 2
        request.session['city_slug'] = 'moskva'
        request.session['city_name'] = 'Москва'