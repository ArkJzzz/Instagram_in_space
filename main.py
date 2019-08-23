#!usr/bin/python3

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

'''
ToDo:
    - назвать репозиторий "Instagram_in_space"

'''

__author__ = 'ArkJzzz (arkjzzz@gmail.com)'


import requests
import os
import logging
import time
import argparse
from os.path import isfile
from os.path import join as joinpath
from dotenv import load_dotenv
from instabot import Bot
from download_picture import download_picture
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_collection
from resize_photos import resize_image



def main():

    # init

    logging.basicConfig(format = u'[LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)

    load_dotenv()
    insta_login = os.getenv("INSTA_LOGIN")
    insta_password = os.getenv("INSTA_PASSWORD")


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_dir = joinpath(BASE_DIR, 'images')

    parser = argparse.ArgumentParser(
        description='Программа автоматизирует сбор фотографий космоса и публикует их в соцсеть Instagram.'
        )

    parser.add_argument(
        '-t', 
        '--timeout', 
        type=int, 
        default=2, 
        help='задержка между публикациями изображений в Instagram (по умолчанию 2 часа)'
    )
    parser.add_argument(
        '-c', 
        '--collections', 
        nargs='*', 
        default='wallpaper', 
        help='введите имена коллекций Hubble (holiday_cards wallpaper spacecraft news printshop stsci_gallery)'
    )

    args = parser.parse_args()

    timeout = 60 * 60 * args.timeout
    hubble_collection_names = [args.collections]


    bot = Bot()
    bot.login(username=insta_login, password=insta_password)


    # do

    fetch_spacex_last_launch(img_dir)

    for collection_name in hubble_collection_names:
        hubble_collection = fetch_hubble_collection(collection_name)

        for image in hubble_collection:
            hubble_url = image['url']
            hubble_filename = 'hubble-{id}'.format(id=image['id'])

            download_picture(hubble_url, img_dir, hubble_filename)


    for image in os.listdir(img_dir):
        if isfile(joinpath(img_dir, image)):
            try:
                resize_image(img_dir, image)
            except FileNotFoundError:
                logging.error('Error: file or dirrectory not found', exc_info=True)
            else:
                path = joinpath(img_dir, image)
                os.remove(path)


    for image in os.listdir(img_dir):
        if isfile(joinpath(img_dir, image)):
            try:
                os.chdir(img_dir)
                bot.upload_photo(image)
            except FileNotFoundError:
                logging.error('Error: file or dirrectory not found', exc_info=True)


        time.sleep(timeout)



if __name__ == '__main__':
    main()