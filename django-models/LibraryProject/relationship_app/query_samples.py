import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query 1: All books by a specific author
    author_name = 'John Doe'
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} not found.")

    print("\n")

    # Query 2: List all books in a library
    library_name = 'Central Library'
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library {library_name} not found.")

    print("\n")

    # Query 3: Retrieve the librarian for a library
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian or Library not found for {library_name}.")

if __name__ == "__main__":
    run_queries()
