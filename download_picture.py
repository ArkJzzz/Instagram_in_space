#!usr/bin/python3

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ArkJzzz (arkjzzz@gmail.com)'


import requests
import os
import sys
import argparse
import logging


def download_picture(url, directory='images', filename=None):
    '''
    Функция принимает на вход url картинки и путь, куда её сохранить, а затем скачивает эту картинку.
    '''
    logging.debug('download_picture():')
    logging.debug(url)
    logging.debug(directory)
    logging.debug(filename)

    network_filename = url.split('/')[-1]
    extension = network_filename.split('.')[-1]

    if filename == None:
        filename = network_filename.split('.')[-2]

    file_path = '{directory}/{filename}.{extension}'.format(
        directory=directory, 
        filename=filename,
        extension=extension 
        )

    logging.debug(file_path)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    response = requests.get(url, verify=False)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)

 

def main():
    logging.basicConfig(format = u'%(levelname)s [LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)

    parser = argparse.ArgumentParser(
        description='Программа принимает на вход url картинки, директорию, куда её сохранить и опционально имя файла, а затем скачивает эту картинку'
        )
    parser.add_argument('url', help='ссылка на картинку')
    parser.add_argument('directory', help='куда сохранять')
    parser.add_argument('-n', '--filename', help='имя файла')
    args = parser.parse_args()

    try:
        download_picture(args.url, args.directory, args.filename)
    except HTTPError:
        logging.error('HTTPError: Not Found', exc_info=True)


if __name__ == "__main__":
    main()