"""
Battle App - Tests
----------------

Test cases for Battle App Routing
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile, ActiveCharacter
from battle.models import ActiveEnemy
import json


class TestViews(TestCase):

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        pswd = "Kavanagh" # noqa
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=pswd)
        logged_in = self.client.login(username=username, password=pswd)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)

        self.assertTrue(logged_in)

    def test_battle_view(self):
        """Tests battle route is rendered with correct context"""
        # Create Active Char
        ActiveCharacter.create_character(self.user, "Dwarf", self.profile.paid)
        # Create Active Enemy
        ActiveEnemy.create_active_enemy(self.profile)
        # Navigate to route and test response/context
        response = self.client.get('/battle/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('character' in response.context)
        self.assertTrue('enemy' in response.context)

    def test_post_battle(self):
        """Tests post-battle route"""
        # Create Active Char
        ActiveCharacter.create_character(self.user, "Dwarf", self.profile.paid)
        # Create Active Enemy
        ActiveEnemy.create_active_enemy(self.profile)
        # Navigate to route and test response/context
        data = {'result': 'true'}
        response = self.client.post('/battle/post_battle/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('outcome' in response.context)
        self.assertTrue(response.context['outcome'])
        self.assertTrue('new_weapon' in response.context)
        self.new_weapon = response.context['new_weapon']

    def test_loot_view(self):
        """Tests Ajax Loot route"""
        # Create Active Char
        ActiveCharacter.create_character(self.user, "Dwarf",
                                         self.profile.paid)

        # Create Json file of new weapon
        newWeapon = {
            'id': 140,
            "base_hp": 10,
            'base_attack': 10,
            'base_defense': 10,
            'base_speed': 10,
            'level': 2,
            'rarity': 2,
        }
        data = json.dumps(newWeapon)
        data = {'newWeapon':  data}
        response = self.client.post(
            '/battle/loot/',
            data,
            **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        )
        self.assertEqual(response.status_code, 200)
        character = ActiveCharacter.objects.get(user=self.user)
        self.assertTrue(character.weapon_id.id == 140)
