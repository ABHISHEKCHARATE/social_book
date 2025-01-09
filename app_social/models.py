from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class SocialUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

class SocialUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    role_choices = (
        ('Author', 'Author'),
        ('Seller', 'Seller'),
    )
    
    role = models.CharField(max_length=6, choices=role_choices,default='Author')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'gender', 'city', 'state']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = SocialUserManager()

    def save(self, *args, **kwargs):
        self.location = f"{self.city}, {self.state}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
  

class Book(models.Model):
    user = models.ForeignKey(SocialUser, on_delete=models.CASCADE, related_name='books')  
    title = models.CharField(max_length=255)  
    author = models.CharField(max_length=255) 
    description = models.TextField()  
    genre = models.CharField(max_length=100) 
    
    file = models.FileField(upload_to='books/files/')  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    extracted_text = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.title
from django.db import models
from django.conf import settings

class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_%(user_id)s/')
