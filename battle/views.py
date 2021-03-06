"""
Battle App - Views
----------------

Views for Battle App.
    - BattleView
    - PostBattleView
    - NewLootView

"""


import json
import copy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from battle.models import ActiveEnemy
from codex.models import Codex
from profiles.functions import calculate_xp, add_weapon
from profiles.models import ActiveCharacter, Profile
from leaderboard.models import Leaderboard


class BattleView(LoginRequiredMixin, TemplateView):
    """
    A View for preparing hero/enemy data as
    both querysets and json objects to be passed
    to the Template.

    Generates new enemy if none currently active in DB.

    """
    template_name = "battle/battle.html"

    def get(self, *args, **kwargs):
        """
        Override Get function to redirect user if no active character
        """
        # Obtain Current Profile
        current_profile = Profile.objects.get(user=self.request.user)
        # If no current character exists, redirect
        if not current_profile.active_char:
            return redirect('profile')
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Override Get_context_data to get user and enemy
        data (generating new enemy if one does not exist),
        and combining this data via queryset and json to the context.
        """

        # Obtain Current Profile
        current_profile = Profile.objects.get(user=self.request.user)

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
        """
        Overrides get_context_data to perform the
        relevant functions depending on whether the user
        wins or loses the battle and subsequently pass the
        appropriate data to the template via the context.
        """
        context = super().get_context_data(**kwargs)

        # Obtain battle outcome from battle page
        context['outcome'] = json.loads(self.request.POST['result'])

        # Query DB for active Character, Profile, and Enemy
        character = ActiveCharacter.objects.get(user=self.request.user)
        current_profile = Profile.objects.get(user=self.request.user)
        enemy = ActiveEnemy.objects.get(active_character=character)

        # If the player won the battle
        if context['outcome']:

            # Add character's current stats to context
            # This is incase the user levels up and can be
            # Used for comparrison on the loot screen
            context['old_stats'] = {
                "hp": character.char_hp,
                "attack": character.char_attack,
                "defense": character.char_defense,
                "speed": character.char_speed
            }

            # Set Active Character Object location in context
            context['active_character'] = character

            # Checks to see whether free user has hit free limit
            if character.current_level == 2 and not current_profile.paid:
                context['free_limit'] = True
            else:
                # Calculate user XP and determine if level up
                if calculate_xp(character, enemy.enemy_level):
                    context['levelled_up'] = True

            # Obtain a new weapon for the user
            context['new_weapon'] = Codex.new_weapon(current_profile.paid,
                                                     character.current_level)

            # Create a deepcopy, to remove and override unserializable
            # fields so object can be passed to Javascript as JSON.
            context['weapon_json'] = copy.deepcopy(
                    context['new_weapon'].__dict__
                    )
            context['weapon_json'].pop('_state')
            context['weapon_json']['image'] = str(context['new_weapon'].image)

            # Delete active enemy
            enemy.delete()

        # If the player has lost the battle
        else:
            # Update profile to reflect changes
            current_profile.active_char = False
            current_profile.total_runs += 1

            # Determine if user has beat own high score
            if current_profile.longest_run < character.battle_count:
                current_profile.longest_run = character.battle_count

            if current_profile.paid:
                # Determine whether score should go in leaderboard
                leaderboard_outcome = Leaderboard.leaderboard_check(character)
                context['leaderboard'], context['score'] = leaderboard_outcome

            # Delete Active Character
            character.delete()

        # Update user's current profile to reflect changes
        current_profile.active_battle = False
        current_profile.save()

        # Return context to post-battle template
        return context

    def post(self, *args, **kwargs):
        """
        Over-ride POST method to ensure user is in battle
        at time of POST, otherwise redirect to Profile.
        """
        current_profile = Profile.objects.get(user=self.request.user)
        if current_profile.active_battle:
            context = self.get_context_data()
            return super().render_to_response(context)
        return redirect('profile')

    def get(self, *args, **kwargs):
        """Override GET request to redirect to profile"""
        return redirect('profile')


class NewLootView(UpdateView):
    """
    View for user to store new weapon.

    View takes AJAX Post request, including
    a modified JSON version of a weapon Codex object.
    This is passed to a custom function to override the
    current user's weapon field, and saves the entry to the DB.
    """
    model = ActiveCharacter

    def post(self, *args, **kwargs):
        """
        Overrides POST method to ensure the request is AJAX,
        Updates the user's active character profile with the
        information received via AJAX, and returns the appropriate HTTP
        responses accoringly.
        """
        if self.request.is_ajax():
            # Obtain Active Character
            character = ActiveCharacter.objects.get(user=self.request.user)
            # Receive Ajax weapon_dict
            weapon_dict = json.loads(self.request.POST['newWeapon'])
            # Update Active Character
            add_weapon(character, weapon_dict)
            return HttpResponse(200)
        return HttpResponse(400)
