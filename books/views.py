from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import NewBookForm
from .models import Book

class BookListView(generic.ListView):
    paginate_by = 3
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)  # get book object
    book_comments = book.comments.all()    # get book comments
    return render(request, 'books/book_detail.html', {'book':book, 'comments':book_comments})


class BookCreateView(generic.CreateView):
    form_class = NewBookForm
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(generic.DeleteView):
    model = Book
    # fields = ['title', 'author', 'brief', 'price']
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(generic.UpdateView):
    model = Book
    # fields = ['title', 'author', 'brief', 'price']
    form_class = NewBookForm
    template_name = 'books/book_update.html'
