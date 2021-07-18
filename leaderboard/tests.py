"""
Leaderboard App - Tests
----------------

Test cases for Leaderboard App Routing
"""

from django.test import TestCase


class TestViews(TestCase):
    def test_leaderboard_page(self):
        """ Test leaderboard view renders correct page """
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard/leaderboard.html')
