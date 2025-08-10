from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Author name must be at least 3 characters long."
            )
        return value


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Book title must be at least 3 characters long."
            )
        return value


# serializers.py# This file contains serializers for the Author and Book models.
# The AuthorSerializer serializes the Author model, while the BookSerializer serializes the Book model and includes a nested AuthorSerializer for the author field.
# The serializers are used to convert model instances into JSON format and validate incoming data for these models.