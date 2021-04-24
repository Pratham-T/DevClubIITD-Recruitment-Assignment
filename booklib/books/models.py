from django.db import models
from django.db.models.base import Model
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Book\'s name')
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    publisher = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=25, help_text='Enter genre of this book', null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of book', null=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 character ISBN number')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across the library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('b', 'Borrowed'),
        ('a', 'Available'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id}({self.book.title})'

    @property
    def is_overdue(self):
        if self.due_back and date.today()>self.due_back:
            return True
        return False


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id), str(self.last_name), str(self.first_name)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class RequestedBooks(models.Model):
    book_id = models.OneToOneField('BookInstance', on_delete=models.RESTRICT, primary_key=True)
    return_date = models.DateField()
    requester = models.ForeignKey(User, on_delete=models.RESTRICT)

    REQUEST_STATUS = (
        ('a', 'Accepted'),
        ('r', 'Rejected'),
        ('p', 'Pending'),
    )

    status = models.CharField(max_length=1, choices=REQUEST_STATUS, default='p', help_text='Borrow Request Status')

    def __str__(self):
        return f'Book: {self.book_id.book.title} ({self.book_id.book.author}), Copy: {self.book_id.id}'

    def remove_rejected():
        rejected_requests = RequestedBooks.objects.filter(status='r')
        rejected_requests.delete()