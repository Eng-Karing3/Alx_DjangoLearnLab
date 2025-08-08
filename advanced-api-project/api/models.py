from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

# models.py# This file contains the definitions for the Author and Book models.
# The Author model has a name field, while the Book model has title, publication_date,
# and a foreign key relationship to the Author model.

