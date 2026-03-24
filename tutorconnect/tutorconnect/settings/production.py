"""
Production settings for TutorConnect UK.

These settings are used when the site is deployed to Heroku.
Security is the priority here.
"""

import os
import dj_database_url
from .base import *

# SECURITY: Never enable debug in production
# Detailed error pages expose code and security vulnerabilities
DEBUG = False

# ALLOWED_HOSTS must include your production domain
# This prevents HTTP Host header attacks
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database Configuration
# dj_database_url parses DATABASE_URL environment variable
# Heroku automatically sets this for PostgreSQL
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,  # Keep connections alive for 10 minutes
    )
}

# Security Settings
# These headers protect against common web vulnerabilities

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Set HSTS header - browser remembers to use HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Cookies only sent over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent browser from guessing content type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser XSS filter
SECURE_BROWSER_XSS_FILTER = True

# Prevent site from being framed (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'

# Email Configuration (we'll use SendGrid)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'noreply@tutorconnect.co.uk')

# Static files configuration for production
# WhiteNoise serves static files efficiently
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Logging for production
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
        'level': 'WARNING',  # Only warnings and errors in production
    },
}