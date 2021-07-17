from django.shortcuts import redirect
from django.views.generic import TemplateView
from profiles.models import ActiveCharacter
from battle.models import ActiveEnemy
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from profiles.functions import calculate_xp
from codex.models import Codex
from profiles.models import Profile


class BattleView(LoginRequiredMixin, TemplateView):
    """
    A View for preparing hero/enemy data as
    both querysets and json objects to be passed
    to the Template.

    Generates new enemy if none currently active in DB.

    """
    template_name = "battle/battle.html"

    def get_context_data(self, **kwargs):

        # Obtain Current Profile
        current_profile = Profile.objects.get(user=self.request.user)

        # If no current character exists, redirect
        if not current_profile.active_char:
            redirect('profile')

        # Default context
        data = super().get_context_data(**kwargs)

        # Obtain active character
        active_character = ActiveCharacter.objects.get(user=self.request.user)

        # Put active character in session
        data['character'] = active_character

        # If the user doesn't have a currently active battle
        if not current_profile.active_battle:
            # Generate enemy
            ActiveEnemy.create_active_enemy(current_profile)

        # Query the Active Enemy DB for user's enemy
        data['enemy'] = ActiveEnemy.objects.get(
            active_character=active_character
            )

        # Serialise character and enemy and return context
        data['json_char'] = serializers.serialize('json', [data['character']])
        data['json_enemy'] = serializers.serialize('json', [data['enemy']])
        return data


class PostBattleView(LoginRequiredMixin, TemplateView):
    """
    A View for post-battle page.

    If the user loses the battle, their Active Character
    is deleted, and the User Profile is deleted to reflect.

    If the user wins the battle, their XP is calculated.
    If they have levelled up, the users stats are upgraded
    to reflect this. Once this has been completed, a
    new weapon is produced to be sent to view.

    Active Enemy is deleted regardless.
    """

    template_name = 'battle/post_battle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtain battle outcome from battle page
        context['outcome'] = json.loads(self.request.POST['result'])

        # Query DB for active Character, Profile, and Enemy
        character = ActiveCharacter.objects.get(user=self.request.user)
        current_profile = Profile.objects.get(user=self.request.user)
        enemy = ActiveEnemy.objects.get(active_character=character)

        # If the player won the battle
        if context['outcome']:

            # Add active character to context
            context['active_character'] = character

            # Calculate user XP and determine if level up
            if calculate_xp(character, enemy.enemy_level):

                # Query DB for new levelled player to add to context
                character = ActiveCharacter.objects.get(user=self.request.user)
                context['levelled_character'] = character

            # Obtain a new weapon for the user
            context['new_weapon'] = Codex.new_weapon(current_profile.paid,
                                                     character.current_level)

            # Update battle stats
            character.battle_count += 1
            character.save()

            # Delete active enemy
            enemy.delete()

        # If the player has lost the battle
        else:
            # Update profile to reflect changes
            current_profile.character = False
            current_profile.total_runs += 1

            # Determine if user has beat own high score
            if current_profile.longest_run < character.battle_count:
                current_profile.longest_run = character.battle_count

            # Delete Active Character
            character.delete()

        # Update user's current profile to reflect changes
        current_profile.active_battle = False
        current_profile.save()

        # Return context to post-battle template
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data()
        return super(PostBattleView, self).render_to_response(context)

    def get(self, request, **kwargs):
        return redirect('profile')
