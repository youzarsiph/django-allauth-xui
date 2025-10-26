"""URLConf for app.books"""

from django.urls import path

from app.books import views


# Create your URlConf here.
urlpatterns = [
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/new/", views.BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/update/", views.BookDetailView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", views.BookDetailView.as_view(), name="book-delete"),
]
