import os
from pathlib import Path

# from django.core.exceptions import ImproperlyConfigured
# from dotenv import load_dotenv

# load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent


# def get_env_variable(var_name):
#     """Get the environment variable or return exception."""
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_msg = f"Set the {var_name} environment variable"
#         raise ImproperlyConfigured(error_msg)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")
SECRET_KEY = "f#@^op=rmq=kx+x5)km2dusdyktl)$==5@h426y+l4%_g%te!q"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = get_env_variable("DJANGO_DEBUG") == "True"
DEBUG = "True"

ALLOWED_HOSTS = [
    "*",  # run on any host
    # "localhost",  # For local development
    # "127.0.0.1",  # For local development
    # "tonybnya.pythonanywhere.com",  # PythonAnywhere web app
    # "portfolio-api-ikc3.onrender.com",  # Your Render domain
]
CSRF_TRUSTED_ORIGINS = ["http://*.on-acorn.io", "https://*.on-acorn.io"]


# Application definition

INSTALLED_APPS = [
    # Default apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # My apps
    "api",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "portfolio.wsgi.application"
# WSGI_APPLICATION = "portfolio.portfolio.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # "default": {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": os.getenv("MARIADB_DATABASE"),
    #     "USER": os.getenv("MARIADB_USER"),
    #     "PASSWORD": os.getenv("MARIADB_ROOT_PASSWORD"),
    #     "HOST": os.getenv("MARIADB_HOST"),
    #     "PORT": os.getenv("MARIADB_PORT", 3306),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
