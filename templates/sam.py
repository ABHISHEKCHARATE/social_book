from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

# Custom User model (optional, can also use Django's built-in User model)
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)  # A field to store both city and state
    
    # Password-related fields
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    
    # Automatically update the location field with city and state
    def save(self, *args, **kwargs):
        self.location = f"{self.city}, {self.state}"
        super(CustomUser, self).save(*args, **kwargs)

    # String representation of the user
    def __str__(self):
        return self.username

    # Optional: Add any other fields or methods as needed.
