from django.shortcuts import render
from .models import *
from django.views import generic


def index(request):
    book_count = Book.objects.all().count() #count(select * from Book)
    author_count = Author.objects.all().count()
    book_instance_count = BookInstance.objects.count()
    book_available_count = BookInstance.objects.filter(status__exact='a').count()
    return render(
        request,
        'index.html',
        context={'book_count': book_count, 'author_count': author_count, 'book_instance_count': book_instance_count, 'book_available_count': book_available_count}
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book





