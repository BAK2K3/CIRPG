"""
Leaderboard App - Tests
----------------

Test cases for Leaderboard App Routing
"""

from django.test import TestCase
from profiles.models import Profile
from .models import Leaderboard
from profiles.models import ActiveCharacter
from django.contrib.auth import get_user_model


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
        
    def test_leaderboard_page(self):
        """ Test leaderboard view renders correct page """
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard/leaderboard.html')

    def test_leaderboard_context(self):
        """ Test empty leaderboard context in page rendering """
        response = self.client.get('/leaderboard/')
        self.assertTrue('leaderboard' in response.context)

    def test_leaderboard_context_contents(self):
        """ Test single leaderboard context entry in page rendering """
        # Create Active Character
        active_char = ActiveCharacter.create_character(self.user,
                                                       "Dwarf",
                                                       self.profile.paid)
        # Call leaderboard check to insert character into leaderboard
        Leaderboard.leaderboard_check(active_char)
        response = self.client.get('/leaderboard/')

        # Ensure context is correct instance, and belongs to user
        leaderboard_entry = response.context['leaderboard'][0]
        self.assertTrue(isinstance(leaderboard_entry, Leaderboard))
        self.assertTrue(leaderboard_entry.user == self.user)
