"""
Profiles App - Tests
----------------

Test cases for Profiles App Routing
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile, ActiveCharacter
from codex.models import Codex


class TestViews(TestCase):

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        password = "Kavanagh"
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=password)
        logged_in = self.client.login(username=username, password=password)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)
        self.assertTrue(logged_in)

    def test_profile_context(self):
        """ Test Current Profile Context being passed to any page"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_profile'].user, self.user)

    def test_character_context(self):
        """ Test Active Character is rendered to Profile page"""
        ActiveCharacter.create_character(self.user, "Dwarf", self.profile.paid)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('character' in response.context)

    def test_create_context(self):
        """ Test Hero list Context being passed to Create page"""
        response = self.client.get('/profile/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['heroes'][0], Codex))

    def test_create_redirect(self):
        """ Test Create page redirects if user has active character """
        self.profile.active_char = True
        self.profile.save()
        response = self.client.get('/profile/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_premium(self):
        """ Test Create route filtering paid from current profile """
        self.profile.active_char = False
        self.profile.paid = True
        self.profile.save()
        response = self.client.get('/profile/create/')
        # Check for all content for paid user
        self.assertTrue(len(response.context['heroes']) == 10)
        self.profile.paid = False
        self.profile.save()
        response = self.client.get('/profile/create/')
        # Check for free content
        self.assertTrue(len(response.context['heroes']) == 3)
