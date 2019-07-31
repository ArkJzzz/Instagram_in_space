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


def fetch_hubble_image_url(hubble_img_id):
    '''
    Функция принимает id снимка Hubble Space Telescope 
    и возвращает ссылку на файл с форматом .jpg, .png или .gif 
    и самым большим разрешением из имеющихся по заданному id 
    '''
    hubble_url = 'http://hubblesite.org/api/v3/image'
    hubble_img_url = '{hubble_url}/{hubble_img_id}'.format(
        hubble_url=hubble_url, 
        hubble_img_id=hubble_img_id
        )
    response = requests.get(hubble_img_url, verify=False)

    hubble_files = response.json()
    hubble_files = hubble_files['image_files']
    hubble_image = {}
    hubble_images = []

    for hubble_file in hubble_files:
        extension = (hubble_file['file_url'].split('/')[-1]).split('.')[-1]
        if extension in ['jpg', 'png', 'gif']:
            hubble_image['file_size'] = hubble_file['file_size']
            hubble_image['file_url'] = hubble_file['file_url']
            hubble_images.append(hubble_image)

    file_sizes = []

    try:
        for hubble_image in hubble_images:
            file_sizes.append(hubble_image['file_size'])
        max_size = max(file_sizes)
        for hubble_image in hubble_images:
            if hubble_image['file_size'] == max_size:
                hubble_image_url = hubble_image['file_url']
            return hubble_image_url
    except Exception:
        logging.error('файлов .jpg, .png или .gif не найдено')


def download_hubble_image(directory, hubble_img_url):
    filename = 'hubble-{index}'.format(index=hubble_img_id)
    download_picture(hubble_img_url, directory, filename)


def fetch_hubble_collection(collection_name):
    hubble_url = 'http://hubblesite.org/api/v3/images/'
    payload = {'collection_name':collection_name}
    
    response = requests.get(hubble_url, params=payload, verify=False)
    response.raise_for_status()

    hubble_images_list = response.json()

    hubble_collection = []
    

    for hubble_image in hubble_images_list:
        hubble_collection_image = {}
        hubble_collection_image['description'] = hubble_image['name']
        hubble_collection_image['id'] = hubble_image['id']
        hubble_collection_image['url'] = 'https:{url}'.format(url=fetch_hubble_image_url(hubble_image['id']))
        hubble_collection.append(hubble_collection_image)

    return hubble_collection

def main():
    parser = argparse.ArgumentParser(
        description='Программа скачивает фотографии, сделанные телескопом HUBBLE, нужно указать коллекцию и папку, куда скачать'
        )
    parser.add_argument('directory', help='куда сохранять')
    parser.add_argument('collection', help='куда сохранять')
    args = parser.parse_args()

    logging.debug('main():')
    logging.debug(args.directory)
    logging.debug(args.collection)


    collection = fetch_hubble_collection(args.collection)
    for image in collection:
    	print(image['url'])
    

if __name__ == "__main__":
    main()