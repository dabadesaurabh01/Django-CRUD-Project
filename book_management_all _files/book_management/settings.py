import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9#v^&*3x@p1!z$g7x0k@c1yq^b2d7jw&4%y5h&7m3qz@r7(0o1'

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'saurabh_book_db',  
        'USER': 'saurabh_user',  
        'PASSWORD': 'Saurabh@123',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
