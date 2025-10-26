"""Main App URLConf"""

from django.urls import path, include

from app import views


# Create your URlConf here.
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    # Auth
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
    # Book urls
    path("", include("app.books.urls")),
]
