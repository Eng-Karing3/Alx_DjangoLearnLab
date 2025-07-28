from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .models import Book
from django.db.models import Q

def book_list(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query)
    ) if query else Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
