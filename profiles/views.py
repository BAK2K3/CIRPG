from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class ProfileDetailView(LoginRequiredMixin, ListView):
    context_object_name = 'profile'
    template_name = "profiles/profile.html"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
