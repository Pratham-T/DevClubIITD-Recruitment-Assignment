from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from django.template import loader
from django.views import generic

from .models import Book, BookInstance, Author

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    latest_book_list = Book.objects.order_by('id')[:5]
    num_authors = Author.objects.all().count()

    template = loader.get_template('books/index.html')
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_avail': num_instances_avail,
        'latest_book_list': latest_book_list,
        'num_authors': num_authors,
    }
    return render(request, 'books/index.html', context=context)

#def detail(request, book_name):
    #book = get_object_or_404(Book, pk=book_name)
    #return render(request, 'books/detail.html', {'book': book})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 15

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15

class AuthorDetailView(generic.DetailView):
    model = Author