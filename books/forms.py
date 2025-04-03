from django import forms
from books.models import Book, Comment


class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'brief', 'price', 'cover']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend', 'is_active')