from django.shortcuts import render
from .models import *
from django.views import generic


def index(request):
    book_count = Book.objects.all().count() #count(select * from Book)
    author_count = Author.objects.all().count()
    book_instance_count = BookInstance.objects.count()
    book_available_count = BookInstance.objects.filter(status__exact='a').count()

    visits_count = request.session.get('visits_count', 0)
    request.session['visits_count'] = visits_count + 1

    return render(
        request,
        'index.html',
        context={'book_count': book_count, 'author_count': author_count, 'book_instance_count': book_instance_count, 'book_available_count': book_available_count, 'visits_count': visits_count}
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(generic.DetailView):
    model = Author





