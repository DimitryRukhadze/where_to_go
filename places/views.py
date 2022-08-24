from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import JsonResponse
from django.urls import reverse


def make_places_geojson():
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        data_for_geojson = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(place.longitude), float(place.latitude)]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place_by_id', args=[place.id])
            }
        }
        places_geojson['features'].append(data_for_geojson)

    return places_geojson


def get_place_by_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_specs = {
        "title": place.title,
        "imgs": [image.img_file.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    return JsonResponse(place_specs)


def index(request):
    context = {
        "geojson": make_places_geojson()
    }
    return render(request, 'index.html', context)
