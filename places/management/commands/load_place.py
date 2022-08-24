import os
import argparse
import json
import shutil
from contextlib import suppress

from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_path', action='store', help='Путь к папке с данными json', type=Path)


    def save_place_imgs(self, imgs_urls, temp_img_folder, place_to_attach):

        for url in imgs_urls:

            response = requests.get(url)
            response.raise_for_status()
            filepath = urlparse(unquote(url)).path
            _, filename = os.path.split(filepath)
            save_path = Path(temp_img_folder, filename)

            with open(save_path, 'wb') as img_file:
                img_file.write(response.content)

            new_image = place_to_attach.images.create(title=filename, place=place_to_attach)
            with open(save_path, 'rb') as img_file:
                new_image.img_file.save(filename, img_file, save=True)


    def handle(self, *args, **options):

        json_file_path = options['json_path']
        for filepath in json_file_path.iterdir():

            with open(filepath, 'rb') as place_specs:
                place = json.load(place_specs)
            try:
                new_place, _ = Place.objects.get_or_create(
                    title=place['title'],
                    description_short=place['description_short'],
                    description_long=place['description_long'],
                    longitude=float(place['coordinates']['lng']),
                    latitude=float(place['coordinates']['lat'])
                )

                temp_img_folder = 'temp_img_folder'
                os.makedirs(temp_img_folder, exist_ok=True)

                try:
                    self.save_place_imgs(place['imgs'], temp_img_folder, new_place)
                except requests.exceptions.HTTPError as error:
                    print(error)
                finally:
                    shutil.rmtree(temp_img_folder)

            except IntegrityError:
                suppress()
