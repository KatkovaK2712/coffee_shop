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
# На Fly.io: задаётся через `fly secrets set SECRET_KEY=...`
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-dev-only-key-do-not-use-in-production'
)

# DEBUG = True только локально. На Fly.io задаётся DEBUG=False.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Разрешённые хосты. На Fly.io автоматически подставляется FLY_APP_NAME.
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
fly_app_name = os.environ.get('FLY_APP_NAME')
if fly_app_name:
    ALLOWED_HOSTS.append(f'{fly_app_name}.fly.dev')
    ALLOWED_HOSTS.append('*')  # на случай прокси-домена

# Доверенные источники для CSRF (формы через HTTPS)
CSRF_TRUSTED_ORIGINS = []
if fly_app_name:
    CSRF_TRUSTED_ORIGINS.append(f'https://{fly_app_name}.fly.dev')


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
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← добавлено для статики
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

LANGUAGE_CODE = 'ru-ru'   # было en-us → сделаем русский

TIME_ZONE = 'Europe/Moscow'  # было UTC → Москва

USE_I18N = True

USE_TZ = True


# ==========================================================
# СТАТИКА И МЕДИА
# ==========================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # куда collectstatic соберёт файлы

# Белый шум — сжимает и отдаёт статику без nginx
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Медиа: сюда Django сохраняет загруженные картинки
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================================================
# ПРОЧЕЕ
# ==========================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'