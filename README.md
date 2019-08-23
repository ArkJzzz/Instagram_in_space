# Instagram_in_space

Автоматизирует сбор фотографий Hubble и SpaceX и публикует их в соцсеть Instagram.


## Установка

1. Клонировать репозиторий:
```
git clone https://github.com/ArkJzzz/Instagram_in_space.git
```

2. Создать файл ```.env``` и поместить в него логин и пароль от аккаунта Instagram:
```
INSTA_LOGIN='Ваш_логин'
INSTA_PASSWORD='Ваш_пароль'
```

3. Установить зависимости: 
```
pip3 install -r requirements.txt
```


## Запуск

Для запуска программы введите:

```
python3 main.py 
```

Можно задать задержку в часах между публикациями изображений в Instagram (по умолчанию 2 часа) с помощью ключа ```-t```. Так же можно задать имена коллекций изображений Hubble через пробел из списка ```(holiday_cards wallpaper spacecraft news printshop stsci_gallery)```(по умолчанию ```wallpaper```) с помощью ключа  ```-c```.

```
python3 main.py -t 24 -c holiday_cards spacecraft printshop
```


## Отдельные скрипты

Есть возможность запуска отдельных частей программы:

### Скачать фотографии с последнего запуска SpaceX (```fetch_spacex.py```)

```
python3 fetch_spacex.py s_img_dir
```

где:

- ```s_img_dir``` - папка, в которую будут загружаться изображения.


### Скачать фотографии, сделанные телескопом HUBBLE (```fetch_hubble.py```)

```
python3 fetch_hubble.py h_img_dir spacecraft
```
где:

- ```h_img_dir``` - папка, в которую будут загружаться изображения;
- ```spacecraft``` - имя коллекции изображений Hubble из списка (holiday_cards wallpaper spacecraft news printshop stsci_gallery).


### Скачать изображение по ссылке (```download_picture.py```)

```python3 download_picture.py  https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png images -n google_logo```

где:

- ```https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png``` - ссылка на изображение;
- ```images``` - папка, в которую нужно сохранить изображение;
- ```google_logo```  - имя, под которым сохранить (опционально, с помощью ключа ```-n```).


### Изменить размер изображения для публикации в Instagram (```resize_photos.py```)

```
python3 resize_photos.py r_img_dir google_logo.png
```
где:

- ```r_img_dir``` - папка, в которой находится файл;
- ```google_logo  .png``` - имя файла.



 