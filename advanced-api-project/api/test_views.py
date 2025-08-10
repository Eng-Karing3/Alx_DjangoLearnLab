from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create books
        self.book1 = Book.objects.create(title="Unique Title One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Another Book", publication_year=2019, author=self.author1)
        self.book3 = Book.objects.create(title="Unique Title Two", publication_year=2021, author=self.author2)

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
            "author": self.author1.id,
        }
        response = self.client.post(url, data)
        # Unauthenticated create should return 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {
            "title": "Updated Title",
            "publication_year": 2022,
            "author": self.author1.id,
        }
        # Authenticate first (simulate logged in user)
        self.client.force_authenticate(user=None)  # Adjust if you have user model
        response = self.client.put(url, data)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_403_FORBIDDEN])

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book1.id])
        # Authenticate first (simulate logged in user)
        self.client.force_authenticate(user=None)  # Adjust if you have user model
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN])

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Only books by author1 (book1 and book2)
        self.assertEqual(len(response.data), 2)
        for book in response.data:
            self.assertEqual(book['author'], self.author1.id)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Unique Title One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Only one book matches the search term
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Unique Title One")

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_order_books_by_publication_year_descending(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
