"""Views for app"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    """Home page"""

    template_name = "app/index.html"


class AboutView(TemplateView):
    """About page"""

    template_name = "app/about.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    """Profile page"""

    template_name = "app/profile.html"
