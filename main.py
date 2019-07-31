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
from os.path import isfile
from os.path import join as joinpath
from dotenv import load_dotenv
from instabot import Bot
from download_picture import download_picture
from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_collection
from resize_photos import resize_image


# logging.basicConfig(format = u'[DEBUG: LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)


def main():

    # init

    load_dotenv()
    insta_login = os.getenv("INSTA_LOGIN")
    insta_password = os.getenv("INSTA_PASSWORD")


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_dir = joinpath(BASE_DIR, 'images')

    hubble_collection_names = [
        # 'holiday_cards'
        'wallpaper'
        # 'spacecraft',
        # 'news',
        # 'printshop',
        # 'stsci_gallery'
        ]

    bot = Bot()
    bot.login(username=insta_login, password=insta_password)

    timeout = 60 * 60 * 2 # 2 часа


    # do

    fetch_spacex_last_launch(img_dir)

    for collection_name in hubble_collection_names:
        hubble_collection = fetch_hubble_collection(collection_name)

        for image in hubble_collection:
            hubble_url = image['url']
            hubble_filename = 'hubble-{id}'.format(id=image['id'])

            download_picture(hubble_url, img_dir, hubble_filename)


    for image in os.listdir(img_dir):
            if isfile(joinpath(img_dir, image)):  #os.path.isfile(path) - является ли путь файлом
                try:
                    resize_image(img_dir, image)
                    path = joinpath(img_dir, image)
                    os.remove(path)
                except Exception as e:
                    pass


    for image in os.listdir(img_dir):
        if isfile(joinpath(img_dir, image)):  #os.path.isfile(path) - является ли путь файлом
            try:
                os.chdir(img_dir)
                bot.upload_photo(image)
            except Exception:
                continue

        time.sleep(timeout)



if __name__ == '__main__':
    main()