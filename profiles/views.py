from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Profile
from codex.models import Codex
from .forms import HiddenForm


class ProfileDetailView(LoginRequiredMixin, ListView):
    """ A View for presenting a user's profile """
    context_object_name = 'profile'
    template_name = "profiles/profile.html"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


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

    def form_valid(self, form):
        print(form.cleaned_data['user_selection'])
        # print(Codex.objects.get_random('Weapon', True, 4))
        return redirect('profile')
