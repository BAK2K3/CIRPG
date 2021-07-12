from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_queryset(self):
        return Codex.objects.filter(type="Hero")
