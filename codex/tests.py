"""
Codex App - Tests
----------------

Test cases for Codex App Routing
"""

from django.test import TestCase


class TestViews(TestCase):
    def test_codex_page(self):
        """ Test codex route renders correct page """
        response = self.client.get('/codex/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/codex.html')

    def test_codex_context(self):
        """ Test codex route queries DB """
        response = self.client.get('/codex/')
        self.assertTrue('codex' in response.context)
