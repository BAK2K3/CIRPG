from django.shortcuts import redirect
from django.views.generic import TemplateView
from profiles.models import ActiveCharacter
from battle.models import ActiveEnemy
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class BattleView(TemplateView):
    """
    A View for preparing hero/enemy data as
    both querysets and json objects to be passed
    to the Template.
    """
    template_name = "battle/battle.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        active_character = ActiveCharacter.objects.get(user=self.request.user)
        data['character'] = active_character
        data['enemy'] = ActiveEnemy.objects.get(
            active_character=active_character
            )
        data['json_char'] = serializers.serialize('json', [data['character']])
        data['json_enemy'] = serializers.serialize('json', [data['enemy']])
        return data


class PostBattleView(LoginRequiredMixin, TemplateView):
    """
    A View for post-battle page.

    View changes depending on outcome of battle.
    
    Outcome of battle influences whether level up
    and new loot is obtained, or whether character
    is deleted.

    Active Enemy is deleted regardless.
    """
    template_name = 'battle/post_battle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outcome'] = json.loads(self.request.POST['result'])

        return context

    def post(self, request, **kwargs):
        context = self.get_context_data()
        return super(PostBattleView, self).render_to_response(context)

    def get(self, request, **kwargs):
        return redirect('profile')
