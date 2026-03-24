"""
Accounts app configuration.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configuration for the accounts application."""
    
    # Full Python path to the app
    # This is different because our app is in the 'apps' folder
    name = 'apps.accounts'
    
    # Human-readable name for admin
    verbose_name = 'User Accounts'
    
    # Default primary key type for models
    default_auto_field = 'django.db.models.BigAutoField'
    
    def ready(self):
        """
        Called when Django starts.
        We'll use this later to import signals.
        """
        # Import signals when app is ready (we'll add this later)
        # import apps.accounts.signals  # noqa
        pass