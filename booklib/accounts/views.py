from django.contrib.auth import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from books.models import BookInstance, RequestedBooks
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('email', 'username',)

@login_required()
class DashboardView(generic.TemplateView):

    def dashboard(request):
        is_Librarian = False
        if request.user.groups.filter(name='Librarian').exists():
            is_Librarian = True

        borrowed_books = BookInstance.objects.filter(borrower = request.user).filter(status__exact='b').order_by('due_back')
        all_borrowed_books = BookInstance.objects.filter(status__exact='b').order_by('due_back')
        requested_books = RequestedBooks.objects.filter(requester__exact = request.user).filter(status__exact='p')
        all_requested = RequestedBooks.objects.filter(status__exact='p')
        
        context = {
            'is_Librarian': is_Librarian,
            'borrowed_books': borrowed_books,
            'all_borrowed_books': all_borrowed_books,
            'requested_books': requested_books,
            'all_requested_books': all_requested,
        }
        
        return render(request, 'accounts/dashboard.html', context=context)

    def borrowRequestAccept(request, id):
        book_inst = BookInstance.objects.get(id=id)
        req_book = RequestedBooks.objects.get(book_id=book_inst)
        req_book.status = 'a'
        req_book.save()
        book_inst.status = 'b'
        book_inst.borrower = req_book.requester
        book_inst.due_back = req_book.return_date
        book_inst.save()
        return HttpResponseRedirect('/accounts/dashboard')
        
    
    def borrowRequestReject(request, id):
        book_inst = BookInstance.objects.get(id=id)
        req_book = RequestedBooks.objects.get(book_id=book_inst)
        req_book.status = 'r'
        req_book.save()
        req_book.delete()
        return HttpResponseRedirect('/accounts/dashboard')

    def returnBook(request, id):
        book_inst = BookInstance.objects.get(id=id)
        book_inst.return_due = None
        book_inst.borrower = None
        book_inst.status = 'a'
        book_inst.save()
        req_book = RequestedBooks.objects.get(book_id=book_inst)
        if req_book:
            if req_book.status=='p':
                req_book.delete()
        return HttpResponseRedirect('/accounts/dashboard')


def registerView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})