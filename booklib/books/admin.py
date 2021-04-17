from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Author, Book, BookInstance

# Register your models here.
admin.site.register(Author)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'genre')
    inlines = [BookInstanceInline]

@register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')