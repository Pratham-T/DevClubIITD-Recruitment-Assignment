from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.BookListView.as_view(), name='books'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/all', views.AuthorListView.as_view(), name='author'),
    path('authors/<int:pk>/<str:last_name>_<str:first_name>/', views.AuthorDetailView.as_view(), name='author_detail')
    #path('<int:id>/', views.detail, name='detail'),
]