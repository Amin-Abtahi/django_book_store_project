from django.contrib import admin
from .models import Book, Comment


@admin.register(Comment)    # this sends the Comment to the admin panel like this : admin.site.register(Comment, CommentAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text','is_active','recommend', 'datetime_created')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'user',)

# admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)
