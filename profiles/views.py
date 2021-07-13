from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Profile
from codex.models import Codex


class ProfileDetailView(LoginRequiredMixin, ListView):
    context_object_name = 'profile'
    template_name = "profiles/profile.html"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class CreateHeroDetailView(LoginRequiredMixin, ListView):
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
