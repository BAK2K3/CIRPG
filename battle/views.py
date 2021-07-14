from django.views.generic import TemplateView
from profiles.models import ActiveCharacter
from battle.models import ActiveEnemy


class BattleView(TemplateView):
    template_name = "battle/battle.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        active_character = ActiveCharacter.objects.get(user=self.request.user)
        context_data['character'] = active_character
        context_data['enemy'] = ActiveEnemy.objects.get(
            active_character=active_character
            )
        return context_data
