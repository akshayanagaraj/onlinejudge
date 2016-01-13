"""
Django settings for judge project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3c0^x3246!hng5=9co_t-8mt6wxiy4+k$kp3)!-jh=z=&s4&5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 
SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.path.join(BASE_DIR,"template"),)

TEMPLATE_CONTEXT_PROCESSORS = (
		'django.core.context_processors.request',
		'django.contrib.auth.context_processors.auth',
		)


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'problems',
    'leaderboard',
    
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.backends.ModelBackend',

)

ROOT_URLCONF = 'judge.urls'

WSGI_APPLICATION = 'judge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "gbatchsec",
        "USERNAME": "root",
        "PASSWORD":'mysql',
        "HOST":'',
        "PORT":'',
	}
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"stat")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


STATICFILES_DIRS = (
	os.path.join(BASE_DIR,"static"),
)
