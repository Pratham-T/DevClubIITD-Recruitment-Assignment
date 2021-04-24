from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from django.template import loader
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Book, BookInstance, Author, RequestedBooks
from .forms import BorrowRequestForm

import datetime

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

@login_required()
def borrow_book_request(request, pk, id):
    book_instance = get_object_or_404(BookInstance, id=id)

    if request.method == 'POST':

        form = BorrowRequestForm(request.POST)

        if form.is_valid():
            return_date = form.cleaned_data['return_date']
            requester = request.user
            requested_book = RequestedBooks(book_id=book_instance, return_date=return_date, requester=requester)
            requested_book.save()

            return response.HttpResponseRedirect(reverse('dashboard'))

    else:
        proposed_return_date = datetime.date.today() + datetime.timedelta(weeks=1)
        form = BorrowRequestForm(initial={'return_date': proposed_return_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'books/book_borrow_request.html', context)



def SearchResults(request):
    book_query = request.GET['book_query']
    author_query = request.GET['author_query']
    
    if book_query:
        books = Book.objects.filter(title__icontains=book_query)
    else:
        books = None
    
    if author_query:
        authors = Author.objects.filter(last_name__icontains=author_query) | Author.objects.filter(first_name__icontains=author_query)
    else:
        authors = None
    
    context = {
        'book_search_results': books,
        'author_search_results': authors,
    }
    return render(request, 'books/search_results.html', context=context)