from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books (Public)
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView: Retrieve a single book by ID (Public)
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView: Add a new book (Authenticated users only)
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Automatically attach the current user's author profile to the book.
        Adjust this logic if Author is not linked to User.
        """
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user.author)


# UpdateView: Modify an existing book (Only the author can update)
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        book = self.get_object()
        if book.author != self.request.user.author:
            raise PermissionDenied("You do not have permission to edit this book.")
        serializer.is_valid(raise_exception=True)
        serializer.save()


# DeleteView: Remove a book (Only the author can delete)
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.author != self.request.user.author:
            raise PermissionDenied("You do not have permission to delete this book.")
        instance.delete()
