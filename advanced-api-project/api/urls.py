from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/', views.ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('books/create/', views.CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.DeleteView.as_view(), name='book-delete'),
]
