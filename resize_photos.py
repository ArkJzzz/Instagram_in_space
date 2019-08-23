#!usr/bin/python3

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ArkJzzz (arkjzzz@gmail.com)'

import logging
import os
import argparse
from os.path import join as joinpath
from PIL import Image


def resize_image(directory, filename):
    target_size = (1024, 1024)
    extention = 'jpg'

    logging.debug('directory: %s' % directory)
    logging.debug('filename: %s' % filename)

    original = Image.open(joinpath(directory, filename))
    original.thumbnail(target_size, Image.ANTIALIAS)

    resized_filename = '{img_filename}-{width}x{hight}.{extention}'.format(
        img_filename = filename.split('.')[-2],
        width = original.size[0],
        hight = original.size[1],
        extention = extention
        )
    resized_filename = joinpath(directory, resized_filename)
    logging.debug('resized_filename: %s' % resized_filename)

    original.save(resized_filename)


def main():
    logging.basicConfig(format = u'%(levelname)s [LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)

    parser = argparse.ArgumentParser(
        description='Программа изменяет размер изображения, укажите директорию и имя файла'
        )
    parser.add_argument('d', help='директория, в которой находится файл')
    parser.add_argument('n', help='имя файла, который нужно изменить')

    args = parser.parse_args()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_dir = joinpath(BASE_DIR, args.d)
    filename = args.n

    try: 
        resize_image(img_dir, filename)
    except FileNotFoundError:
        logging.error('Error: file or dirrectory not found', exc_info=True)

if __name__ == "__main__":
    main()