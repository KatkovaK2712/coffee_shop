"""
Django settings for coffee_shop project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# БЕЗОПАСНОСТЬ
# ==========================================================

# SECRET_KEY читается из переменной окружения.
# Локально: если переменной нет — используется dev-ключ.
# На Render: задаётся через Environment Variables.
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-dev-only-key-do-not-use-in-production'
)

# DEBUG = True только локально. На Render задаётся DEBUG=False.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ==========================================================
# ХОСТЫ
# ==========================================================
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']


# ==========================================================
# ПРИЛОЖЕНИЯ
# ==========================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cafe',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # для статики на продакшене
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coffee_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coffee_shop.wsgi.application'


# ==========================================================
# БАЗА ДАННЫХ (SQLite)
# ==========================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==========================================================
# ВАЛИДАЦИЯ ПАРОЛЕЙ
# ==========================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==========================================================
# ЛОКАЛИЗАЦИЯ
# ==========================================================

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# ==========================================================
# СТАТИКА И МЕДИА
# ==========================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise — сжимает и отдаёт статику без nginx
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Медиа: сюда Django сохраняет загруженные картинки
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================================
# ПРОЧЕЕ
# ==========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================================================
# ПРОКСИ (для Render)
# ==========================================================

# Render работает через прокси и передаёт протокол в заголовке
# X-Forwarded-Proto. Без этих настроек Django не понимает, что запрос
# пришёл по HTTPS, и может отклонять его с ошибкой 400 Bad Request.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Разрешаем Django использовать заголовок X-Forwarded-Host,
# который прокси Render подставляет автоматически.
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True