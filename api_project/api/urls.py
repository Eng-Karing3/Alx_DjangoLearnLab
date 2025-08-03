from django.contrib import admin
from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'), 
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)
]


