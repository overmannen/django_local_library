from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author, Genre, Language
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_instances = BookInstance.objects.count()

    num_instances_available = BookInstance.objects.filter(status__exact="a").count()
    num_romance = Genre.objects.filter(name__contains="romance").count()

    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_romance": num_romance,
        "num_visits": num_visits,
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


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""

    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_user.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by("due_back")
        )


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = "catalog.can_mark_returned"
    template_name = "catalog/bookinstance_list_borrowed_all.html"

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact="o").order_by("due_back")
