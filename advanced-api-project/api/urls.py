from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListView.as_view(), name='book-list'),                # GET all books (with filtering/searching/ordering)
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),    # GET single book
    path('books/create/', views.CreateView.as_view(), name='book-create'),      # POST new book
    path('books/update/<int:pk>/', views.UpdateView.as_view(), name='book-update'),  # PUT/PATCH update book
    path('books/delete/<int:pk>/', views.DeleteView.as_view(), name='book-delete'),  # DELETE book
]
