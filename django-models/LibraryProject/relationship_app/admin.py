from django.contrib import admin
from .models import Author, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)


# Register your models here.
