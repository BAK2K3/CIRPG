"""
Codex App - Views
----------------

Views for Codex App.
    - CodexListView
    - CodexUpdateView
    - CodexCreateView
    - CodexDeleteView

"""

# pylint: disable=r0901

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Codex
from .forms import CodexForm
from .functions import process_codex_url


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pre_context = None

    def get_queryset(self):
        """
        Override get_queryset to extract GET Params
        and apply the subsequent search and sort parameters
        to the query.
        """

        # Extract context parameters from request
        self.pre_context = process_codex_url(self.request.GET)

        # Apply search and sort params to queryset
        query = Codex.objects.filter_queryset(
            search_params=self.pre_context['search_params'],
            sort_params=self.pre_context['sort_params']
            )
        return query

    def get_context_data(self, **kwargs):
        """
        Override get_context_data to merge default
        context data with prepared context.
        """

        # Merge default context with prepared context params
        context = super().get_context_data(**kwargs) | self.pre_context
        return context


class CodexUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to provide a Form to the user
    pre-filled with existing Codex Data.
    """
    form_class = CodexForm
    template_name = "codex/edit.html"
    success_url = "/codex/"
    model = Codex

    def test_func(self):
        return self.request.user.is_superuser


class CodexCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    A view to provide a Form to the user
    to create a Codex entry.
    """
    form_class = CodexForm
    template_name = "codex/create.html"
    success_url = "/codex/"
    model = Codex

    def test_func(self):
        return self.request.user.is_superuser


class CodexDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete Codex entries.
    """
    success_url = "/codex/"
    model = Codex

    def test_func(self):
        """
        Tests the method is post and user is superuser.
        """
        if self.request.method == "POST":
            return self.request.user.is_superuser
        return self.get(self.request)

    def get(self, *args, **kwargs):
        """
        Redirects get requests to the Codex view.
        """
        return redirect('codex')
