"""
Tests for the accounts app.

Run tests with: python manage.py test apps.accounts
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserManagerTests(TestCase):
    """Test cases for the CustomUserManager."""
    
    def test_create_user_with_email(self):
        """Test creating a regular user with email."""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User'
        )
        
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
        self.assertEqual(user.user_type, User.UserType.STUDENT)
        self.assertFalse(user.is_email_verified)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)
    
    def test_create_user_without_email_raises_error(self):
        """Test that creating a user without email raises ValueError."""
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='testpass123')
    
    def test_create_superuser(self):
        """Test creating a superuser."""
        admin_user = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
            first_name='Admin',
            last_name='User'
        )
        
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)
    
    def test_email_normalized(self):
        """Test that email domain is normalized to lowercase."""
        user = User.objects.create_user(
            email='test@EXAMPLE.COM',
            password='testpass123'
        )
        self.assertEqual(user.email, 'test@example.com')


class CustomUserModelTests(TestCase):
    """Test cases for the CustomUser model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            email='student@example.com',
            password='testpass123',
            first_name='John',
            last_name='Doe',
            user_type=User.UserType.STUDENT
        )
        
        self.tutor = User.objects.create_user(
            email='tutor@example.com',
            password='testpass123',
            first_name='Jane',
            last_name='Smith',
            user_type=User.UserType.TUTOR
        )
    
    def test_string_representation(self):
        """Test the __str__ method returns full name."""
        self.assertEqual(str(self.user), 'John Doe')
    
    def test_get_full_name(self):
        """Test get_full_name method."""
        self.assertEqual(self.user.get_full_name(), 'John Doe')
    
    def test_get_short_name(self):
        """Test get_short_name method returns first name."""
        self.assertEqual(self.user.get_short_name(), 'John')
    
    def test_is_student_property(self):
        """Test is_student property for student user."""
        self.assertTrue(self.user.is_student)
        self.assertFalse(self.user.is_tutor)
    
    def test_is_tutor_property(self):
        """Test is_tutor property for tutor user."""
        self.assertTrue(self.tutor.is_tutor)
        self.assertFalse(self.tutor.is_student)
    
    def test_can_book_lessons(self):
        """Test that students can book lessons but tutors cannot."""
        self.assertTrue(self.user.can_book_lessons())
        self.assertFalse(self.tutor.can_book_lessons())
    
    def test_can_offer_tutoring(self):
        """Test that tutors can offer tutoring but students cannot."""
        self.assertTrue(self.tutor.can_offer_tutoring())
        self.assertFalse(self.user.can_offer_tutoring())
