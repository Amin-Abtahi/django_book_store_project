from django import forms
from books.models import Book


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'brief', 'price', 'cover']