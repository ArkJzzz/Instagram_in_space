#!usr/bin/python3

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ArkJzzz (arkjzzz@gmail.com)'


import os
import requests
import argparse
import logging
from download_picture import download_picture



def fetch_spacex_last_launch(directory):
    spacex_url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(spacex_url)
    spacex_images_urls = response.json()
    spacex_images_urls = spacex_images_urls['links']
    spacex_images_urls = spacex_images_urls['flickr_images']

    if not directory:
        directory = 'SpaceX_images'
    
    for index, spacex_images_url in enumerate(spacex_images_urls):
        filename = 'spacex-{index}'.format(index=index)
        download_picture(spacex_images_url, directory, filename)


def main():
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии с последнего запуска SpaceX, нужно указать только папку, куда скачать'
        )
    parser.add_argument('directory', help='куда сохранять')
    args = parser.parse_args()

    logging.debug('main():')
    logging.debug(args.directory)

    fetch_spacex_last_launch(args.directory)
    

if __name__ == "__main__":
    main()