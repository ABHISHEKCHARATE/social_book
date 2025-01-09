# """
# Django settings for social_books project.

# Generated by 'django-admin startproject' using Django 5.1.4.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """
# import os

# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATES_DIR= os.path.join(BASE_DIR,'templates')
# STATIC_DIR= os.path.join(BASE_DIR,'static')
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-f$$mf8z6n0o5mx6kt%3k1h-*^=+lx)*^+&rbzf-ks$32!1)t+c"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# # Application definition

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     'app_social',
# ]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "social_books.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         'DIRS': [
#             TEMPLATES_DIR,  
#         ],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "social_books.wsgi.application"


# # Database
# # https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.1/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'app_social', 'static')


# STATIC_ROOT = BASE_DIR /"staticfiles_build"/"static/"

# MEDIA_URL= 'images/'


# # Add STATIC_DIR to STATICFILES_DIRS
# STATICFILES_DIRS = [
#     STATIC_DIR,
# ]

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# MEDIA_DIR = os.path.join(BASE_DIR, 'media')  

SECRET_KEY = "django-insecure-f$$mf8z6n0o5mx6kt%3k1h-*^=+lx)*^+&rbzf-ks$32!1)t+c"
DEBUG = True
ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'app_social.SocialUser' 
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'app_social',
    'rest_framework',
    'rest_framework.authtoken',  
    'djoser',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# EMAIL_HOST_USER = 'charateabhishek3@gmail.com'
# EMAIL_HOST_PASSWORD = 'AbhiCharate_123'


EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'charateabhishek3@gmail.com') 
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'AbhiCharate_123')  

EMAIL_HOST_PASSWORD = 'gpqb dajp fqzc njle'  





# DJOSER = {
#     'LOGIN_FIELD': 'username',  
# }


# DJOSER = {
#     'TOKEN_MODEL': 'rest_framework.authtoken.models.Token', 
# }

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "social_books.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "social_books.wsgi.application"

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'social',
'USER': 'postgres',
'PASSWORD': '123',
'HOST': 'localhost',
'PORT': '5432',

}
}



AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

BASE_DIRR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is where media files will be stored, pointing to 'books/media' folder
MEDIA_URL = '/media/'

# Absolute path to the directory where media files will be stored
MEDIA_ROOT = os.path.join(BASE_DIRR, 'books', 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'