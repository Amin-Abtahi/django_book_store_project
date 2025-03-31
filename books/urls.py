from django.urls import path

from books.views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookDeleteView,
    BookUpdateView
)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book_update'),


]