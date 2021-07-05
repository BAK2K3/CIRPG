"""
Codex App - Tests
----------------

Test cases for Codex App Routing
"""

from django.test import TestCase
from codex.models import Codex
from random import randint


class TestViews(TestCase):

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def test_codex_page(self):
        """ Test codex route renders correct page """
        response = self.client.get('/codex/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/codex.html')

    def test_codex_context(self):
        """ Test codex route queries DB """
        response = self.client.get('/codex/')
        self.assertTrue('codex' in response.context)

    def test_codex_entry_structure(self):
        """ Test codex db entry structure"""
        response = self.client.get('/codex/')
        self.assertTrue(isinstance(response.context['codex'][0], Codex))

    def test_codex_query_premium(self):
        """Test codex filtering for premium products """
        response = self.client.get('/codex/?premium=1')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.paid)

    def test_codex_query_free(self):
        """Test codex filtering for free products """
        response = self.client.get('/codex/?premium=0')
        codex_entry = response.context['codex'][0]
        self.assertFalse(codex_entry.paid)

    def test_codex_query_weapon(self):
        """Test codex filtering for weapons """
        response = self.client.get('/codex/?type=weapon')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Weapon")

    def test_codex_query_enemies(self):
        """Test codex filtering for enemies """
        response = self.client.get('/codex/?type=enemy')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Enemy")

    def test_codex_query_heroes(self):
        """Test codex filtering for heroes """
        response = self.client.get('/codex/?type=hero')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Hero")

    def test_codex_query_level(self):
        """Test codex filtering for rating"""
        random_rating = str(randint(1, 5))
        response = self.client.get(f'/codex/?levels={random_rating}')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level == int(random_rating))

    def test_codex_query_multilevel(self):
        """Test codex filtering for multiple ratings"""
        response = self.client.get('/codex/?levels=2%2C3')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level in [2, 3])

    def test_codex_multi_query(self):
        """Test codex filtering for multiple parameters"""
        response = self.client.get('/codex/?premium=0&type=weapon&levels=1')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level == 1)
        self.assertTrue(not codex_entry.paid)
        self.assertTrue(codex_entry.type == "Weapon")
