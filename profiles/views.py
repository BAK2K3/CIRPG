"""
Profiles App - Views
----------------

Views for Profiles App.
    - ProfileDetailView
    - CreateHeroDetailView
    - CreateHeroFormView
    - HeroDeleteView
"""

# pylint: disable=r0901

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import FormView, DetailView, DeleteView
from codex.models import Codex
from .models import Profile, ActiveCharacter
from .forms import HiddenForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """ A View for presenting a user's profile """
    context_object_name = 'character'
    template_name = "profiles/profile.html"

    def get_object(self, *args, **kwargs):
        """
        Override get_object to return active character
        if it exists, otherwise return None.
        """
        if Profile.objects.get(user=self.request.user).active_char:
            return ActiveCharacter.objects.get(user=self.request.user)
        return None


class CreateHeroDetailView(LoginRequiredMixin, ListView):
    """A view for creating a new hero"""
    context_object_name = 'heroes'
    template_name = "profiles/create.html"

    def dispatch(self, request, *args, **kwargs):
        """Override dispatch for redirect if active_char exists for user"""
        current_profile = get_object_or_404(Profile, user=self.request.user)
        if current_profile.active_char:
            return redirect('profile')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Override Queryset to obtain characters available to user"""
        current_profile = get_object_or_404(Profile, user=self.request.user)
        return Codex.objects.hero_select(current_profile.paid)

    def get_context_data(self, **kwargs):
        """Override get_context_data to add hidden form to context"""
        context = super().get_context_data(**kwargs)
        context['form'] = HiddenForm()
        return context


class CreateHeroFormView(LoginRequiredMixin, FormView):
    """A view for hero submission"""
    form_class = HiddenForm

    def form_valid(self, form):
        """On valid form submission, create an Active Character"""
        paid = self.request.session['user_paid']
        hero_name = form.cleaned_data['user_selection']
        ActiveCharacter.create_character(user=self.request.user,
                                         hero_name=hero_name,
                                         paid=paid)
        return redirect('profile')


class HeroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """A view for deleting an Active Character"""
    model = ActiveCharacter

    def get_object(self, queryset=None):
        """Obtain the user's active character"""
        user_pk = self.request.POST.get('pk')
        return self.get_queryset().filter(pk=user_pk).get()

    def test_func(self):
        """Ensure user is owner of object on POST"""
        if self.request.method == "POST":
            return self.get_object().user == self.request.user
        return self.get(self.request)

    def get_success_url(self):
        """Amend Active Char attribute before redirect"""
        Profile.remove_active_char(user=self.request.user)
        return reverse_lazy('profile')

    def get(self, *args, **kwargs):
        """Redirect User to profile regardless for get req"""
        return redirect('profile')
