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
    """
    Unit Tests for Profiles App Views

    setUp - Create test login user and create Profile entry

    UT03 - Test Current Profile Context being passed to any page
    UT04 - Test Active Character is rendered to Profile page
    UT05 - Test Hero list Context being passed to Create page
    UT06 - Test Create page redirects if user has active character
    UT07 - Test Create route filtering paid from current profile
    UT08 - Test Create Character post submission route
    UT09 - Test Delete Character route deletes active Char

    """

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        pswd = "Kavanagh" # noqa
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username=username,
                                                   password=pswd)
        logged_in = self.client.login(username=username, password=pswd)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)
        self.assertTrue(logged_in)

    def test_profile_context(self):
        """ UT03 - Test Current Profile Context being passed to any page"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['current_profile'].user, self.user)

    def test_character_context(self):
        """ UT04 - Test Active Character is rendered to Profile page"""
        ActiveCharacter.create_character(self.user, "Dwarf", self.profile.paid)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('character' in response.context)

    def test_create_context(self):
        """ UT05 - Test Hero list Context being passed to Create page"""
        response = self.client.get('/profile/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['heroes'][0], Codex))

    def test_create_redirect(self):
        """ UT06 - Test Create page redirects if user has active character """
        self.profile.active_char = True
        self.profile.save()
        response = self.client.get('/profile/create/')
        self.assertEqual(response.status_code, 302)

    def test_create_premium(self):
        """ UT07 - Test Create route filtering paid from current profile """
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

    def test_create_character_post(self):
        """ UT08 - Test Create Character post submission route"""
        # Create required post_dict for POST
        post_dict = {
            "user_selection": "Dwarf"
        }
        # Navigate to the required view and submit the form
        self.client.get('/profile/create/')
        self.client.post('/profile/create_submit/', post_dict)

        # Naviagte to profile view
        response = self.client.get('/profile/')

        # Test the returned context is an active_char entry
        active_char = response.context['character']
        self.assertTrue(active_char.user.username == "Ben")
        self.assertTrue(active_char.character_id.name == "Dwarf")

        # Re-assign self.profile to updated Profile to check active_char
        self.profile = Profile.objects.get(user=self.user)
        self.assertTrue(self.profile.active_char)

    def test_delete_character(self):
        """ UT09 - Test Delete Character route deletes active Char"""
        # Create a Character
        new_char = ActiveCharacter.create_character(self.user,
                                                    "Dwarf",
                                                    self.profile.paid)
        self.profile.active_char = True
        # Create required post dict
        post_dict = {
            "pk": new_char.pk
        }
        # Navigate to profile, and post to delete_hero
        self.client.get('/profile/')
        self.client.post('/profile/delete_hero/', post_dict)

        # Navigate to profile and make sure no active_char in context
        response = self.client.get('/profile/')
        self.assertTrue('character' not in response.context)

        # Re-assign self.profile to updated Profile to check active_char
        self.profile = Profile.objects.get(user=self.user)
        self.assertFalse(self.profile.active_char)
