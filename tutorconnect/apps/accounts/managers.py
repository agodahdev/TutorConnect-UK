"""
Custom User Manager for email-based authentication.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of username.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.
        
        Args:
            email (str): User's email address (required)
            password (str): User's password (optional, but should be set)
            **extra_fields: Any additional fields for the user model
            
        Returns:
            User: The created user instance
            
        Raises:
            ValueError: If email is not provided
            
        Example:
            user = User.objects.create_user(
                email='student@example.com',
                password='securepassword123',
                first_name='John',
                last_name='Doe'
            )
        """
        # Validate that email is provided
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        # Normalize email: lowercase the domain part
        # 'John@EXAMPLE.com' becomes 'John@example.com'
        email = self.normalize_email(email)
        
        # Create user instance (not saved to DB yet)
        user = self.model(email=email, **extra_fields)
        
        # Set password using Django's built-in hashing
        # NEVER store plain text passwords!
        user.set_password(password)
        
        # Save to database
        # using=self._db ensures we use the correct database
        # (important for multi-database setups)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        
        Superusers have all permissions and can access Django admin.
        
        Args:
            email (str): Admin's email address
            password (str): Admin's password
            **extra_fields: Additional fields
            
        Returns:
            User: The created superuser instance
        """
        # Set default values for superuser flags
        extra_fields.setdefault('is_staff', True)      # Can access admin
        extra_fields.setdefault('is_superuser', True)  # Has all permissions
        extra_fields.setdefault('is_active', True)     # Account is active
        
        # Verify the flags are set correctly
        # (in case someone passes is_staff=False)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        # Use our create_user method
        return self.create_user(email, password, **extra_fields)