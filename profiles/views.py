from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import FormView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Profile, ActiveCharacter
from codex.models import Codex
from .forms import HiddenForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """ A View for presenting a user's profile """
    context_object_name = 'character'
    template_name = "profiles/profile.html"

    def get_object(self):
        if Profile.objects.get(user=self.request.user).active_char:
            return ActiveCharacter.objects.get(user=self.request.user)


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
        paid = self.request.session['paid']
        new_weapon = Codex.objects.get_random('Weapon', paid, 1)
        new_hero = Codex.objects.get(name=form.cleaned_data['user_selection'])
        ActiveCharacter.create_character(user=self.request.user,
                                         hero=new_hero,
                                         weapon=new_weapon)

        return redirect('profile')
