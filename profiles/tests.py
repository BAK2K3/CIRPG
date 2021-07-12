"""
Profiles App - Tests
----------------

Test cases for Profiles App Routing
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile


class TestViews(TestCase):

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        password = "Kavanagh"
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=password)
        logged_in = self.client.login(username=username, password=password)

        # Add User to Profile
        Profile.objects.create(user=self.user)

        # Test Login
        self.assertTrue(logged_in)

    def test_profile_context(self):
        """ Test Profile Context being passed to Profile page"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'][0].user, self.user)
