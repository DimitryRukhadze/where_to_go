import os
import shutil

from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from places.models import Place


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            action='store',
            help='Путь к папке с данными json'
        )

    def save_place_imgs(self, imgs_urls, temp_img_folder, place_to_attach):
        for url in imgs_urls:
            response = requests.get(url)
            response.raise_for_status()
            filepath = urlparse(unquote(url)).path
            _, filename = os.path.split(filepath)
            save_path = Path(temp_img_folder, filename)

            with open(save_path, 'wb') as img_file:
                img_file.write(response.content)

            new_image = place_to_attach.images.create(place=place_to_attach)
            with open(save_path, 'rb') as img_file:
                new_image.img_file.save(filename, img_file, save=True)

    def handle(self, *args, **options):

        json_files_url = options['json_url']

        response = requests.get(json_files_url)
        response.raise_for_status()

        place_data = response.json()
        try:
            new_place, _ = Place.objects.get_or_create(
                title=place_data['title'],
                description_short=place_data['description_short'],
                description_long=place_data['description_long'],
                longitude=float(place_data['coordinates']['lng']),
                latitude=float(place_data['coordinates']['lat'])
            )

            temp_img_folder = 'temp_img_folder'
            os.makedirs(temp_img_folder, exist_ok=True)

            try:
                self.save_place_imgs(
                    place_data['imgs'],
                    temp_img_folder,
                    new_place
                )
            except requests.exceptions.HTTPError as error:
                print(error)
            finally:
                shutil.rmtree(temp_img_folder)
        except IntegrityError:
            print('This place already exists in the database')
