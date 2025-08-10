from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2005, author=self.author1)
        self.book3 = Book.objects.create(title="Book Three", publication_year=2010, author=self.author2)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_single_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book_requires_authentication(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author1.id
        }
        response = self.client.post(url, data, format='json')
        # Should be 403 or 401 depending on your permission setup
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2021,
            "author": self.author1.id
        }
        # Authenticate first if your API requires it; otherwise, skip auth
        # For this test, assume no auth required or adjust as needed
        response = self.client.put(url, data, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book1.id])
        # Same as above regarding auth
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Three'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Three')

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
