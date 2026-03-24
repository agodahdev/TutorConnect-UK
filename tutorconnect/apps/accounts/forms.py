"""
Forms for user registration and profile management.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating new users.
    
    Used in Django admin and can be used in custom registration views.
    Extends UserCreationForm which handles password confirmation.
    """
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_type')
        
    def __init__(self, *args, **kwargs):
        """
        Customize form initialization.
        
        Add CSS classes and placeholders for better UX.
        """
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Customize specific fields
        self.fields['email'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'


class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating user accounts.
    
    Used in Django admin for editing existing users.
    """
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'user_type', 
                  'is_email_verified', 'phone_number')


class StudentRegistrationForm(UserCreationForm):
    """
    Registration form specifically for students.
    
    Students don't need to choose user_type - it's automatically set.
    """
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Add placeholders
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
    
    def save(self, commit=True):
        """
        Save the user with student user_type.
        
        Override save to automatically set user_type to STUDENT.
        """
        user = super().save(commit=False)
        user.user_type = CustomUser.UserType.STUDENT
        
        if commit:
            user.save()
        
        return user


class TutorRegistrationForm(UserCreationForm):
    """
    Registration form specifically for tutors.
    
    Tutors automatically get user_type=TUTOR.
    We also collect phone number as it's important for tutors.
    """
    
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        help_text=_('Optional. Students may need to contact you.'),
    )
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number',
                  'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # Add placeholders
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Phone number (optional)'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
    
    def save(self, commit=True):
        """
        Save the user with tutor user_type.
        """
        user = super().save(commit=False)
        user.user_type = CustomUser.UserType.TUTOR
        
        if commit:
            user.save()
        
        return user


class UserProfileForm(forms.ModelForm):
    """
    Form for users to update their profile information.
    
    This is a basic form - tutors will have an extended profile form.
    """
    
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'