from django.views.generic import TemplateView
from profiles.models import ActiveCharacter
from battle.models import ActiveEnemy
from django.core import serializers


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
