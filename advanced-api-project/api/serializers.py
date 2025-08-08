from .models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author']


# serializers.py# This file contains serializers for the Author and Book models.
# The AuthorSerializer serializes the Author model, while the BookSerializer serializes the Book model and includes a nested AuthorSerializer for the author field.
# The serializers are used to convert model instances into JSON format and validate incoming data for these models.