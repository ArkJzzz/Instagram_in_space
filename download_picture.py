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

logging.basicConfig(format = u'[LINE:%(lineno)d]#  %(message)s', level = logging.DEBUG)



def download_picture(url, directory, filename=None):
    '''
    Функция принимает на вход url картинки и путь, куда её сохранить, а затем скачивает эту картинку.
    '''
    logging.debug('download_picture():')
    logging.debug(url)
    logging.debug(directory)
    logging.debug(filename)

    if not directory:
        directory = 'images'


    if filename != None:
        filename = filename
    else:
        filename = (url.split('/')[-1]).split('.')[-2]

    extension = (url.split('/')[-1]).split('.')[-1]

    file_path = '{directory}/{filename}.{extension}'.format(
        directory=directory, 
        filename=filename,
        extension=extension 
        )

    logging.debug(file_path)

    try:
        os.makedirs(os.path.dirname(file_path))
    except FileExistsError:
        print('directory already exists')
    response = requests.get(url, verify=False)
    with open(file_path, 'wb') as file:
        file.write(response.content)

 

def main():
    parser = argparse.ArgumentParser(
        description='Программа принимает на вход url картинки, директорию, куда её сохранить и опционально имя файла, а затем скачивает эту картинку'
        )
    parser.add_argument('url', help='ссылка на картинку')
    parser.add_argument('directory', help='куда сохранять')
    parser.add_argument('-n', '--filename', help='имя файла')
    args = parser.parse_args()

    download_picture(args.url, args.directory, args.filename)


if __name__ == "__main__":
    main()