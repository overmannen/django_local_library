from django.shortcuts import render
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
