"""
Django settings for online_shop project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ws3bs3o$xw9vqhtmzveway!j4jed3x6^i^%pqr2)t&%ko3kkli'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '178.62.220.138',
#    u'178.62.220.138',
    'calm-studio.ru',
    'www.calm-studio.ru',

]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'main',
    'blog',
    'shop',
    'checkout',
    'taggit',
    'paypal.standard.ipn',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            (os.path.join(BASE_DIR, 'main/templates/tracking')),
            (os.path.join(BASE_DIR, 'blog/templates/tracking')),
            (os.path.join(BASE_DIR, 'shop/templates/tracking')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.getting_cart_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main/static'),
    os.path.join(BASE_DIR, 'blog/static'),
    os.path.join(BASE_DIR, 'shop/static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'main/static/db')
MEDIA_URL = '/media/'

SITE_ID = 4

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_POST = 469

EMAIL_HOST_USER = 'whitenight.info@mail.ru'
EMAIL_HOST_PASSWORD = 'ghjcvjnhtnmgjxne'

EMAIL_USE_TLS = True

######################################
    ## PAYPAL ##
#####################################

PAYPAL_RECEIVER_EMAIL = 'artem.pif@mail.ru'
PAYPAL_TEST = True