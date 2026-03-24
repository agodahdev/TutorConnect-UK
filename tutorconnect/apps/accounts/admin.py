"""
Admin configuration for the accounts app.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for our User model.
    
    We override several attributes to work with our email-based
    authentication and custom fields.
    """
    
    # Fields to display in the user list view
    list_display = (
        'email',
        'first_name', 
        'last_name',
        'user_type',
        'is_email_verified',
        'is_active',
        'date_joined',
    )
    
    # Fields that can be used to filter the list
    list_filter = (
        'user_type',
        'is_email_verified',
        'is_active',
        'is_staff',
        'date_joined',
    )
    
    # Fields that can be searched
    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    
    # Default ordering in list view
    ordering = ('-date_joined',)
    
    # Make email verified status editable from list view
    list_editable = ('is_email_verified',)
    
    # Fields displayed when viewing/editing a user
    # Organized into collapsible fieldsets
    fieldsets = (
        # Main section - no title
        (None, {
            'fields': ('email', 'password')
        }),
        # Personal info section
        (_('Personal Info'), {
            'fields': ('first_name', 'last_name', 'phone_number')
        }),
        # Account type section
        (_('Account Type'), {
            'fields': ('user_type', 'is_email_verified', 'profile_complete')
        }),
        # Permissions section (collapsible)
        (_('Permissions'), {
            'classes': ('collapse',),  # Makes this section collapsible
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        # Important dates section (collapsible)
        (_('Important Dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined', 'updated_at'),
        }),
    )
    
    # Fields displayed when ADDING a new user
    # (different from editing because password needs special handling)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Extra CSS class for wider form
            'fields': (
                'email',
                'first_name',
                'last_name',
                'user_type',
                'password1',
                'password2',
            ),
        }),
    )
    
    # Fields that should be read-only
    readonly_fields = ('date_joined', 'last_login', 'updated_at')