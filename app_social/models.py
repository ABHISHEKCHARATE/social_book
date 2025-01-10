from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import date
from datetime import date, datetime  
from django.core.exceptions import ValidationError

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



from datetime import date, datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class SocialUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    role_choices = (
        ('Author', 'Author'),
        ('Seller', 'Seller'),
    )
    role = models.CharField(max_length=6, choices=role_choices, default='Author')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True,default=None)
    age = models.PositiveIntegerField(null=True, blank=True, editable=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'full_name', 'city', 'state']

    objects = SocialUserManager()

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            if isinstance(self.date_of_birth, str):
                try:
                    self.date_of_birth = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
                except ValueError:
                    raise ValidationError("Invalid date format. Expected YYYY-MM-DD.")

            today = date.today()
            self.age = (
                today.year - self.date_of_birth.year
                - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
            )
        else:
            self.age = None

        super().save(*args, **kwargs)

    @property
    def location(self):
        return f"{self.city}, {self.state}"

    def __str__(self):
        return f"{self.username} ({self.role})"



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
from django.core.validators import URLValidator

class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_%(user_id)s/')



class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_url = models.CharField(max_length=500)  # Use CharField for flexibility
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Validate file_url as either a URL or a local file path
        try:
            URLValidator()(self.file_url)  # Check if it's a valid URL
        except ValidationError:
            if not self.file_url.startswith('C:/') and not self.file_url.startswith('file:///'):
                raise ValidationError("Enter a valid URL or local file path.")

    def __str__(self):
        return f"{self.file_name} uploaded by {self.user.username}"