"""
Base settings for TutorConnect UK project.
These settings are shared across all environments (development, production).

"""

import os
from pathlib import Path

# python-dotenv loads variables from .env file into environment
# This keeps sensitive data (API keys, passwords) out of code
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'
# BASE_DIR points to the project root (where manage.py lives)
# .parent.parent because we're now in tutorconnect/settings/base.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from .env file
# The .env file should NEVER be committed to git (it contains secrets)
load_dotenv(BASE_DIR / '.env')

# SECURITY WARNING: keep the secret key used in production secret!
# os.getenv() reads from environment variables
# The second argument is a fallback default (only for development)
SECRET_KEY = os.getenv('SECRET_KEY', 'your-development-secret-key-change-in-production')

# Application definition
# These are Django's built-in apps that provide core functionality
DJANGO_APPS = [
    'django.contrib.admin',          # Admin interface
    'django.contrib.auth',           # Authentication system
    'django.contrib.contenttypes',   # Content type framework
    'django.contrib.sessions',       # Session framework
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static file handling
    'django.contrib.sites',          # Sites framework (needed for allauth)
]

# Third-party apps we'll add later
THIRD_PARTY_APPS = [
    # 'allauth',                     # We'll add these as we progress
    # 'allauth.account',
    # 'crispy_forms',
    # 'crispy_bootstrap5',
]

# Our custom apps - we'll add these as we create them
LOCAL_APPS = [
    # 'apps.core',
    # 'apps.accounts',
    # 'apps.tutors',
    # 'apps.bookings',
    # 'apps.reviews',
    # 'apps.payments',
]

# Combine all apps
# Order matters! Django apps first, then third-party, then local
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware - processes requests/responses
# Think of middleware as layers an onion - request goes through each layer
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # Security checks
    'django.contrib.sessions.middleware.SessionMiddleware', # Session handling
    'django.middleware.common.CommonMiddleware',            # Common operations
    'django.middleware.csrf.CsrfViewMiddleware',            # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # User auth
    'django.contrib.messages.middleware.MessageMiddleware', # Flash messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection
]

# URL configuration - tells Django where to find URL patterns
ROOT_URLCONF = 'tutorconnect.urls'

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Where Django looks for templates
        'DIRS': [BASE_DIR / 'templates'],
        # Also look in each app's templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            # Context processors add variables to every template
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application path
WSGI_APPLICATION = 'tutorconnect.wsgi.application'

# Password validation
# These validators ensure users create strong passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        # Prevents passwords too similar to user attributes
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Minimum length requirement
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Prevents common passwords like "password123"
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Prevents all-numeric passwords
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-gb'  # British English
TIME_ZONE = 'Europe/London'  # UK timezone
USE_I18N = True  # Enable translations
USE_TZ = True  # Use timezone-aware datetimes

# Static files (CSS, JavaScript, Images)
# URL prefix for static files
STATIC_URL = '/static/'

# Additional directories to look for static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Where collectstatic will gather all static files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sites framework (required for django-allauth)
SITE_ID = 1

# Custom User Model - we'll create this soon
# AUTH_USER_MODEL = 'accounts.CustomUser'

# Login/Logout URLs
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'