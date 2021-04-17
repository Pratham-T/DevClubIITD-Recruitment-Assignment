from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from django.template import loader

from .models import Book

# Create your views here.
def index(request):
    latest_book_list = Book.objects.order_by('id')[:5]
    template = loader.get_template('books/index.html')
    context = {
        'latest_book_list': latest_book_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, book_name):
    book = get_object_or_404(Book, pk=book_name)
    return render(request, 'books/detail.html', {'book': book})