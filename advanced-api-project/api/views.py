from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer


# List and Create Books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]  # Anyone can list books
        return [permissions.IsAuthenticated()]  # Create requires login

    def perform_create(self, serializer):
        # Here you could validate or modify data before saving
        if not serializer.validated_data.get('title'):
            raise PermissionDenied("Title is required.")
        serializer.save()  # Save book as provided


# Retrieve, Update, and Delete a single Book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]  # Only logged-in users can update/delete
        return [permissions.AllowAny()]  # Anyone can view a book

    def perform_update(self, serializer):
        # Example: reject updates with empty title
        if not serializer.validated_data.get('title'):
            raise PermissionDenied("Book title cannot be empty.")
        serializer.save()

# Create your views here.
