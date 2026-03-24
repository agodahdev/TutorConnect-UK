"""
Development settings for TutorConnect UK.

These settings are used when developing locally.
NEVER use these settings in production!

"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG=True shows detailed error pages with code snippets
# This is helpful for debugging but exposes sensitive info in production
DEBUG = True

# ALLOWED_HOSTS defines which domains can serve this site
# In development, we only need localhost
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# SQLite is perfect for development - no setup required
# It's a single file database stored in your project folder
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Email Configuration
# In development, we print emails to the console instead of sending them
# This lets you see verification emails, password resets, etc.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django Debug Toolbar (optional but helpful)
# Uncomment when you install django-debug-toolbar
# INSTALLED_APPS += ['debug_toolbar']
# MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
# INTERNAL_IPS = ['127.0.0.1']

# Crispy Forms (we'll add this later)
# CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
# CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Logging configuration for development
# Shows SQL queries in console (helpful for debugging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',  # Shows SQL queries
            'handlers': ['console'],
        },
    },
}