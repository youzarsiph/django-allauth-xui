"""Generic view mixins"""


# Create your mixins here.
class OwnerMixin:
    """Adds the owner of the object"""

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user

        return super().form_valid(form)


class UserFilterMixin:
    """Filters the queryset by user"""

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
