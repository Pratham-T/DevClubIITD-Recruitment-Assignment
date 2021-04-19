from django.db import models
from django.urls import reverse
import uuid


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

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id}({self.book.title})'


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id), str(self.last_name), str(self.first_name)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'