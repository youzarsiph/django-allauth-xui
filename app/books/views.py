"""Views for app.books"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from app.mixins import OwnerMixin, UserFilterMixin
from app.books.models import Book


# Create your views here.
class BookCreateView(OwnerMixin, LoginRequiredMixin, generic.CreateView):
    """Create a book"""

    model = Book
    fields = ["title", "description"]
    success_url = reverse_lazy("books:book_list")


class BookListView(generic.ListView):
    """Display a list of books"""

    model = Book


class BookDetailView(generic.DetailView):
    """Display a book"""

    model = Book


class BookUpdateView(UserFilterMixin, LoginRequiredMixin, generic.UpdateView):
    """Update a book"""

    model = Book
    fields = ["title", "description"]
    success_url = reverse_lazy("books:book_list")


class BookDeleteView(UserFilterMixin, LoginRequiredMixin, generic.DeleteView):
    """Delete a book"""

    model = Book
    success_url = reverse_lazy("books:book_list")
