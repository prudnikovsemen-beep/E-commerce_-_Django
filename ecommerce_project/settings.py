import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# --- ОТЛАДКА: вывод переменных БД (УДАЛИТЬ ПЕРЕД ЗАЛИВКОЙ НА СЕРВЕР!) ---
# Это полезно, чтобы убедиться, что .env подхватился и пароли верные
print("--- Проверка подключения к БД ---")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_HOST: {os.getenv('DB_HOST', 'localhost')}")
print(f"DB_PORT: {os.getenv('DB_PORT', '5432')}")
# Не выводим пароль в явном виде даже в логах отладки
print("---------------------------------")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gyc45nm154&-bk*$$t^!emo%b38i7)4asc_$0ple-j@7l8lm7q'

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Твое приложение каталога
    'catalog',
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

ROOT_URLCONF = 'ecommerce_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ecommerce_project.wsgi.application'

# --- БАЗА ДАННЫХ (PostgreSQL) ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": int(os.environ.get("DB_PORT", 5432)),
        "OPTIONS": {
            "options": "-c client_encoding='UTF8'",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru-ru'  # Для твоего блога и e-commerce лучше сразу ru-ru
TIME_ZONE = 'Europe/Moscow'  # Чтобы даты (created_at/updated_at) были по твоему времени
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

# --- МЕДИАФАЙЛЫ (ОБЯЗАТЕЛЬНО ДЛЯ IMAGEFIELD) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Email (оставил как у тебя, пригодится для ботов)
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
