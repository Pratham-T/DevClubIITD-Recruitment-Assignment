from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Author, Book, BookInstance, RequestedBooks

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
    list_display = ('book', 'status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

@register(RequestedBooks)
class RequestedBooksAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'status', 'requester', 'return_date')

    actions = ['borrow_request_accept', 'borrow_request_reject']

    @admin.action(description='Mark selected books as approved for borrowing')
    def borrow_request_accept(self, request, queryset):
        queryset.update(status='a')
        for query in queryset:
            query.book_id.status = 'b'
            query.book_id.borrower = query.requester
            query.book_id.due_back = query.return_date
            query.book_id.save()

    @admin.action(description='Mark selected books as rejected for borrowing')
    def borrow_request_reject(self, request, queryset):
        queryset.update(status='r')
        for query in queryset:
            query.delete()