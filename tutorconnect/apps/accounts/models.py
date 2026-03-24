"""
Custom User Model for TutorConnect UK.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User model that uses email for authentication.
    
    Inherits from AbstractUser which provides:
    - password
    - last_login
    - is_superuser
    - is_staff
    - is_active
    - date_joined
    - first_name
    - last_name
    
    We add:
    - email (as primary identifier)
    - user_type (Student, Tutor, Admin)
    - is_email_verified
    - phone_number
    
    Attributes:
        email (str): User's email address (unique, used for login)
        user_type (str): Type of user account
        is_email_verified (bool): Whether email has been verified
        phone_number (str): Optional contact number
    """
    
    # User type choices - stored in database as short codes
    # but displayed as readable names in forms/admin
    class UserType(models.TextChoices):
        """
        Enum-like class for user types.
        
        Learning Point: TextChoices creates a set of valid options.
        First value is stored in DB, second is human-readable.
        """
        STUDENT = 'STUDENT', _('Student')
        TUTOR = 'TUTOR', _('Tutor')
        ADMIN = 'ADMIN', _('Admin')
    
    # Remove username field - we're using email instead
    username = None
    
    # Email field - our primary identifier
    email = models.EmailField(
        _('email address'),
        unique=True,  # No two users can have the same email
        error_messages={
            'unique': _('A user with this email already exists.'),
        },
        help_text=_('Required. Enter a valid email address.'),
    )
    
    # User type - determines permissions and dashboard views
    user_type = models.CharField(
        _('user type'),
        max_length=10,
        choices=UserType.choices,
        default=UserType.STUDENT,
        help_text=_('Determines the user\'s role and permissions.'),
    )
    
    # Email verification status
    is_email_verified = models.BooleanField(
        _('email verified'),
        default=False,
        help_text=_('Whether the user has verified their email address.'),
    )
    
    # Phone number (optional)
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        blank=True,  # Field is optional
        help_text=_('Contact phone number (optional).'),
    )
    
    # Profile completion tracking
    profile_complete = models.BooleanField(
        _('profile complete'),
        default=False,
        help_text=_('Whether the user has completed their profile setup.'),
    )
    
    # Timestamps
    updated_at = models.DateTimeField(
        _('updated at'),
        auto_now=True,  # Automatically set on every save
    )
    
    # Configure the custom manager
    objects = CustomUserManager()
    
    # Tell Django to use email for authentication
    USERNAME_FIELD = 'email'
    
    # Fields required when creating superuser via command line
    # (email is automatically required since it's USERNAME_FIELD)
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    class Meta:
        """Model metadata."""
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # Order users by date joined (newest first)
        ordering = ['-date_joined']
    
    def __str__(self):
        """
        String representation of the user.
        
        Returns the full name if available, otherwise email.
        This is shown in Django admin and when printing the object.
        """
        return self.get_full_name() or self.email
    
    def get_full_name(self):
        """
        Return the user's full name.
        
        Returns:
            str: First name + last name, stripped of whitespace
        """
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name or self.email
    
    def get_short_name(self):
        """
        Return the user's first name.
        
        Returns:
            str: First name or email if no first name
        """
        return self.first_name or self.email.split('@')[0]
    
    # ==========================================
    # Helper Methods for User Type Checking
    # ==========================================
    
    @property
    def is_student(self):
        """Check if user is a student."""
        return self.user_type == self.UserType.STUDENT
    
    @property
    def is_tutor(self):
        """Check if user is a tutor."""
        return self.user_type == self.UserType.TUTOR
    
    @property
    def is_admin_user(self):
        """
        Check if user is an admin.
        Note: Different from is_staff which controls Django admin access.
        """
        return self.user_type == self.UserType.ADMIN
    
    def can_book_lessons(self):
        """
        Check if user can book lessons.
        
        Only students and admins can book lessons.
        Tutors cannot book lessons with other tutors (in this version).
        """
        return self.is_student or self.is_admin_user
    
    def can_offer_tutoring(self):
        """
        Check if user can offer tutoring services.
        
        Only tutors can offer tutoring.
        """
        return self.is_tutor