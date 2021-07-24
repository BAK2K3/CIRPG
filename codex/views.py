from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Codex
from .functions import process_codex_url
from .forms import CodexForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class CodexListView(ListView):
    """
    A view to return all entries within codex.
    View takes parameters for both sorting and searching.
    These paremeters are then returned to the view for
    template logic.
    """

    # Override default model/template/context name
    model = Codex
    template_name = 'codex/codex.html'
    context_object_name = 'codex'

    # Override get_queryset
    def get_queryset(self):

        # Extract context parameters from request
        self.pre_context = process_codex_url(self.request.GET)

        # Apply search and sort params to queryset
        q = Codex.objects.filter_queryset(self.pre_context['search_params'],
                                          self.pre_context['sort_params'])
        return q

    # Override get_queryset
    def get_context_data(self, **kwargs):

        # Merge default context with prepared context params
        context = super().get_context_data(**kwargs) | self.pre_context
        return context


class CodexUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    pre-filled with existing Form Data.
    """
    form_class = CodexForm
    template_name = "codex/edit.html"
    success_url = "codex/codex.html"
    model = Codex

    def test_func(self):
        return self.request.user.is_superuser
