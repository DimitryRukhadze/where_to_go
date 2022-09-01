import os

from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            action='store',
            help='Путь к папке с данными json'
        )

    def save_place_imgs(self, imgs_urls, place_to_attach):
        for url in imgs_urls:
            response = requests.get(url)
            response.raise_for_status()

            filepath = urlparse(unquote(url)).path
            _, filename = os.path.split(filepath)
            file_content = response.content

            img_file = ContentFile(file_content)

            place_image = place_to_attach.images.create(place=place_to_attach)
            place_image.img_file.save(filename, img_file, save=True)

    def handle(self, *args, **options):

        json_files_url = options['json_url']

        response = requests.get(json_files_url)
        response.raise_for_status()

        place_data = response.json()
        place_obj, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'description_short': place_data.get('description_short', ''),
                'description_long': place_data.get('description_long', ''),
                'longitude': float(place_data['coordinates']['lng']),
                'latitude': float(place_data['coordinates']['lat'])
            }
        )

        try:
            self.save_place_imgs(
                place_data['imgs'],
                place_obj
            )
        except requests.exceptions.HTTPError as error:
            print(error)

        if not created:
            print(f'{place_obj} has been updated')
