import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(find_dotenv())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery.apps.GalleryConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'povsite.urls'

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

WSGI_APPLICATION = 'povsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ("ru", "Русский"),
    ("en", "English"),
    ("fr", "French"),
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR, 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SERVER_EMAIL = 'artyomkolesnikov1990@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[ТОЧКИ ЗРЕНИЯ]'
SERVER_EMAIL = "capitas.kolesnikov@yandex.ru"

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "capitas.kolesnikov"
EMAIL_HOST_PASSWORD = "qsrhucnxsjkvcjvs"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "capitas.kolesnikov@yandex.ru"

ADMINS = [('Andrey Gunyavin', 'artyomkolesnikov1990@gmail.com'), ]  # TODO change email

# логирование
LOGGING = {
    # первый ключ version всегда определяется как 1
    'version': 1,
    # контролирует работу существующей (стандартной) схемы логирования
    'disable_existing_loggers': False,
    'style': '{',
    # ключ — формат записи сообщений
    'formatters': {
        # (выводим в консоль) формат сообщения уровня DEBUG+ — время, уровень сообщения, сообщение
        'console_simple': {'format': '%(asctime)s %(levelname)s %(message)s'},
        # (выводим в консоль) формат сообщения уровня WARNING+ — время, уровень сообщения, сообщение, путь к источнику события
        'console_warning': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'},
        # (выводим в консоль) формат сообщения уровня ERROR и CRITICAL — время, уровень сообщения, сообщение, путь к источнику события, стэк ошибки
        'console_error': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'},
        # (выводим в файл general.log) формат сообщения уровня INFO+ — время, уровень сообщения, модуль, сообщение
        'general': {'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
        # (выводим в файл errors.log) формат сообщения уровня ERROR и CRITICAL — время, уровень сообщения, сообщение, путь к источнику события, стэк ошибки
        'error': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'},
        # (выводим в файл security.log) формат сообщения "уровня" SECURITY — время, уровень сообщения, модуль, сообщение
        'security': {'format': '%(asctime)s %(levelname)s %(module)s %(message)s'},
        # (отправляем на почту) формат сообщения уровня ERROR+ — время, уровень сообщения, сообщение, путь к источнику события
        'email': {'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
                  },
    },
    # ключ — фильтры
    'filters': {
        # в консоль сообщения отправляются только при DEBUG = True
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
        # на почту и в файл general.log — только при DEBUG = False
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
    },
    # ключ — обработчики
    'handlers': {
        # обработчик вывода сообщений уровня DEBUG+ в консоль
        'console_simple': {
            # уровень применения
            'level': 'DEBUG',
            # применяемый фильтр
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_simple'},
        # обработчик вывода сообщений уровня WARNING+ в консоль
        'console_warning': {
            # уровень применения
            'level': 'WARNING',
            # применяемый фильтр
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_warning'},
        # обработчик вывода сообщений уровня ERROR и CRITICAL в консоль
        'console_error': {
            # уровень применения
            'level': 'ERROR',
            # применяемый фильтр
            'filters': ['require_debug_true'],
            # обработчик, отправляющий сообщения в консоль
            'class': 'logging.StreamHandler',
            # применяемый формат вывода
            'formatter': 'console_error'},
        # обработчик вывода сообщений уровня INFO+ в файл general.log
        'general': {
            # уровень применения
            'level': 'INFO',
            # применяемый фильтр
            'filters': ['require_debug_false'],
            # обработчик, отправляющий сообщения в файл
            'class': 'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'general.log',
            # применяемый формат вывода
            'formatter': 'general'},
        # обработчик вывода сообщений уровня ERROR+ в файл errors.log
        'error': {
            # уровень применения
            'level': 'ERROR',
            # обработчик, отправляющий сообщения в файл
            'class': 'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'errors.log',
            # применяемый формат вывода
            'formatter': 'error'},
        # обработчик вывода сообщений, связанных с безопасностью (security), в файл security.log
        'security': {
            # уровень применения
            'level': 'DEBUG',
            # обработчик, отправляющий сообщения в файл
            'class': 'logging.FileHandler',
            # имя файла, в который отправляем сообщение
            'filename': 'security.log',
            # применяемый формат вывода
            'formatter': 'security'},
        # обработчик вывода сообщений уровня ERROR+, отправляемых по почте
        'mail_admins': {
            # уровень применения
            'level': 'ERROR',
            # применяемый фильтр
            'filters': ['require_debug_false'],
            # обработчик, отправляющий сообщения по почте
            'class': 'django.utils.log.AdminEmailHandler',
            # применяемый формат вывода
            'formatter': 'email'
        },
    },
    # ключ — логгеры
    'loggers': {
        #  регистратор
        'django': {
            # отправляет на консоль и в файл
            'handlers': ['console_simple', 'console_warning', 'console_error', 'general'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.request': {
            # отправляет в файл и на почту
            'handlers': ['error', 'mail_admins'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.server': {
            # отправляет в файл и на почту
            'handlers': ['error', 'mail_admins'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.template': {
            # отправляет в файл
            'handlers': ['error'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.db.backends': {
            # отправляет в файл
            'handlers': ['error'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        },
        # регистратор
        'django.security': {
            # отправляет в файл
            'handlers': ['security'],
            # сообщения логгера по иерархии (родительским логгерам)
            'propagate': True,
        }
    }
}
