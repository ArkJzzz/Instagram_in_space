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

    try:
        response.raise_for_status()
    except HTTPError:
        logging.error('HTTPError: Not Found', exc_info=True)
    else:
        hubble_files = response.json()
        hubble_files = hubble_files['image_files']
        hubble_images = []

        for hubble_file in hubble_files:
            network_filename = hubble_file['file_url'].split('/')[-1]
            extension = network_filename.split('.')[-1]
            if extension in ['jpg', 'png', 'gif']:
                hubble_image = {
                    'file_size': hubble_file['file_size'],
                    'file_url': hubble_file['file_url']   
                }
                hubble_images.append(hubble_image)
    
    try:
        file_sizes = [hubble_image['file_size'] for hubble_image in hubble_images]
        max_size = max(file_sizes)

        for hubble_image in hubble_images:
            if hubble_image['file_size'] == max_size:
                return hubble_image['file_url'] 
    except FileNotFoundError:     
        logging.error('файлов .jpg, .png или .gif не найдено', exc_info=True)


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
        hubble_collection_image = {
            'description': hubble_image['name'],
            'id': hubble_image['id'],
            'url': 'https:{url}'.format(url=fetch_hubble_image_url(hubble_image['id']))
        }

        hubble_collection.append(hubble_collection_image)

    return hubble_collection

def main():
    logging.basicConfig(format = u'%(levelname)s [LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)

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