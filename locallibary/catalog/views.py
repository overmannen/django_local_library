from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre, Language


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_romance = Genre.objects.filter(name__contains="romance").count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_romance": num_romance,
    }

    return render(request, "index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 1


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1


class AuthorDetailView(generic.DetailView):
    model = Author
