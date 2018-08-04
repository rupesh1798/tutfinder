"""
Django settings for tutfinder project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e&9!tyxvdtil^y)rl95=ixo9j5kfl%gv49v5k64+teok2hcqh9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'tutfinder-api.ap-south-1.elasticbeanstalk.com', 'www.tutfinder-api.ap-south-1.elasticbeanstalk.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',

    'rest_framework',
    'djoser',

    'course',
    'core',
    'review',
    'technology',
    'track',
    'track_course',
    'profile',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']

ROOT_URLCONF = 'tutfinder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tutfinder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),

]

CORS_ORIGIN_ALLOW_ALL = True
#setting upload paths for ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
#ckeditor uses pillow for image backend
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
    },
}
#saw it some where
CKEDITOR_ALLOW_NONIMAGE_FILES = True


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         # 'rest_framework.authentication.SessionAuthentication',
#     ),
# }

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # )
    "DEFAULT_AUTHENTICATION_CLASSES": (
        #'rest_framework.authentication.SessionAuthentication',
        #'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #'rest_framework.authentication.BasicAuthentication'

    ),
    "DEFAULT_PERMISSION_CLASSES": (
        'rest_framework.permissions.AllowAny',
        #'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='gonoobieteam@gmail.com'
EMAIL_HOST_PASSWORD = 'teamadmin123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS=True
#EMAIL_USE_SSL = False
#EMAIL_HOST= 'smtp.sendgrid.net'
#EMAIL_HOST_USER='apikey'
#EMAIL_HOST_PASSWORD='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'
#EMAIL_PORT=587
#EMAIL_HOST = 'smtp.sendgrid.net''smtp.gmail.com'
#EMAIL_HOST_USER = 'yourusername@youremail.com''gonoobieteam@gmail.com'
#EMAIL_HOST_PASSWORD = 'your password''teamadmin123'
#EMAIL_PORT = 465
#EMAIL_USE_TLS = True
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS=True
#EMAIL_USE_SSL = False
#EMAIL_HOST= 'email-smtp.us-west-2.amazonaws.com'
#EMAIL_HOST_USER='AKIAIABMXBRDUSHATXOA'
#EMAIL_HOST_PASSWORD='AgPIqcTPkG50VhLwbe90E6RT/jYsgfCxXrDFNAHuGpfu'
#EMAIL_PORT=587

DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'PASSWORD_RESET_CONFIRM_RETYPE' : True,
    #'LOGOUT_ON_PASSWORD_CHANGE': True, https://tag1consulting.com/blog/building-api-django-20-part-i
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://test.localhost/']
}


JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}

"""
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=200),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('JWT', 'Bearer'),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}"""
