from rest_framework import serializers
from .models import SocialUser
from .models import Book


class SocialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialUser
        fields = ['id', 'email', 'username', 'full_name', 'role', 'city', 'state', 'date_of_birth', 'age', 'location']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'genre', 'file', 'extracted_text', 'created_at', 'updated_at']
