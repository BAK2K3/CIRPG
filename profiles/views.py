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

    # Override dispatch for CBV/Redirect
    def dispatch(self, request, *args, **kwargs):
        current_profile = get_object_or_404(Profile, user=self.request.user)
        if current_profile.active_char:
            return redirect('profile')
        else:
            return super(CreateHeroDetailView, self).get(request,
                                                         *args,
                                                         **kwargs)

    def get_queryset(self):
        current_profile = get_object_or_404(Profile, user=self.request.user)
        return Codex.objects.hero_select(current_profile.paid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HiddenForm()
        return context


class CreateHeroFormView(LoginRequiredMixin, FormView):
    """A view for hero submission"""
    form_class = HiddenForm

    # On valid form, create an Active Character
    def form_valid(self, form):
        paid = self.request.session['user_paid']
        hero_name = form.cleaned_data['user_selection']
        ActiveCharacter.create_character(user=self.request.user,
                                         hero_name=hero_name,
                                         paid=paid)
        return redirect('profile')


class HeroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """A view for deleting an Active Character"""
    model = ActiveCharacter

    # Obtain the user's active character
    def get_object(self, queryset=None):
        pk = self.request.POST.get('pk')
        return self.get_queryset().filter(pk=pk).get()

    # Ensure user is owner of object on POST
    def test_func(self):
        if self.request.method == "POST":
            return self.get_object().user == self.request.user
        else:
            return self.get(self.request)

    # Amend Active Char attribute before redirect
    def get_success_url(self):
        Profile.remove_active_char(user=self.request.user)
        return reverse_lazy('profile')

    # Redirect User to profile regardless for get req
    def get(self, request=None):
        return redirect('profile')
