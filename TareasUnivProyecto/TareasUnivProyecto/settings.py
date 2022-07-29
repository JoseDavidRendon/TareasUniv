"""
Django settings for TareasUnivProyecto project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


from email.policy import strict
import os
from pathlib import Path
import mimetypes
mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&zzy-@ljf7gu$5^b(xyv=0et7-0o+0*)&zjmglyhs-n#1im2tq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
 
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'index',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]
 
ROOT_URLCONF = 'TareasUnivProyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TareasUnivProyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5hpfsmuii2att',
        'USER': 'ckxpbwtckwgrkk',
        'PASSWORD': 'be61391c2f8fce7f910533b837c53f3e54fa62669507604de302fd75ccf824ae',
        'HOST': 'ec2-44-205-41-76.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'TareasUnivProyecto/static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = "/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP  = os.path.join(BASE_DIR, 'static') 
#STATIC_URL  = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'melishamta2@gmail.com'
EMAIL_HOST_PASSWORD = 'azytdnchdzfeotey'
EMAIL_USE_TLS = True


# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_HTTPONLY: True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PEROLAD = True
SECURE_SSL_REDIRECT=True #desactivar para test
SECURE_BROWSER_XSS_FILTER=True
SECURE_HSTS_PRELOAD=True
CACHES={
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'Cache_django_web',
    }
} 