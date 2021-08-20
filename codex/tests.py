"""
Codex App - Tests
----------------

Test cases for Codex App Routing
"""

from django.test import TestCase
from codex.models import Codex
from random import randint
from django.contrib.auth import get_user_model
from profiles.models import Profile


class TestViews(TestCase):
    """
    Unit Tests for Codex App Views

    setUp - Create test login user and create Profile entry

    UT23 - Test codex route renders correct page
    UT24 - Test codex route queries DB
    UT25 - Test codex db entry structure
    UT26 - Test codex filtering for premium products
    UT27 - Test codex filtering for free products
    UT28 - Test codex filtering for weapons
    UT29 - Test codex filtering for enemies
    UT30 - Test codex filtering for heroes
    UT31 - Test codex filtering for rating
    UT32 - Test codex filtering for multiple ratings
    UT33 - Test codex filtering for multiple parameters
    UT34 - Test codex sorting direction parameters
    UT35 - Test codex sort by parameters
    UT36 - Test codex Edit view
    UT37 - Test codex Create view
    UT38 - Test codex Delete view
    """

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        pswd = "Kavanagh" # noqa
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=pswd,
                                             is_superuser=True)
        logged_in = self.client.login(username=username, password=pswd)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)

        self.assertTrue(logged_in)

    def test_codex_page(self):
        """ UT23 - Test codex route renders correct page """
        response = self.client.get('/codex/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/codex.html')

    def test_codex_context(self):
        """ UT24 - Test codex route queries DB """
        response = self.client.get('/codex/')
        self.assertTrue('codex' in response.context)

    def test_codex_entry_structure(self):
        """ UT25 - Test codex db entry structure"""
        response = self.client.get('/codex/')
        self.assertTrue(isinstance(response.context['codex'][0], Codex))

    def test_codex_query_premium(self):
        """ UT26 - Test codex filtering for premium products """
        response = self.client.get('/codex/?premium=1')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.paid)

    def test_codex_query_free(self):
        """ UT27 - Test codex filtering for free products """
        response = self.client.get('/codex/?premium=0')
        codex_entry = response.context['codex'][0]
        self.assertFalse(codex_entry.paid)

    def test_codex_query_weapon(self):
        """ UT28 - Test codex filtering for weapons """
        response = self.client.get('/codex/?type=weapon')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Weapon")

    def test_codex_query_enemies(self):
        """ UT29 - Test codex filtering for enemies """
        response = self.client.get('/codex/?type=enemy')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Enemy")

    def test_codex_query_heroes(self):
        """ UT30 - Test codex filtering for heroes """
        response = self.client.get('/codex/?type=hero')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.type == "Hero")

    def test_codex_query_level(self):
        """ UT31 - Test codex filtering for rating """
        random_rating = str(randint(1, 5))  # nosec
        response = self.client.get(f'/codex/?levels={random_rating}')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level == int(random_rating))

    def test_codex_query_multilevel(self):
        """ UT32 - Test codex filtering for multiple ratings """
        response = self.client.get('/codex/?levels=2%2C3')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level in [2, 3])

    def test_codex_multi_query(self):
        """ UT33 - Test codex filtering for multiple parameters """
        response = self.client.get('/codex/?premium=0&type=weapon&levels=1')
        codex_entry = response.context['codex'][0]
        self.assertTrue(codex_entry.min_level == 1)
        self.assertTrue(not codex_entry.paid)
        self.assertTrue(codex_entry.type == "Weapon")

    def test_codex_sort_dir(self):
        """ UT34 - Test codex sorting direction parameters """
        response = self.client.get('/codex/?direction=desc')
        sort_dir = response.context['sort_dir']
        codex = response.context['codex']
        codex_length = len(codex)
        self.assertTrue(sort_dir == 'desc')
        self.assertTrue(codex[0].pk == codex_length)

    def test_codex_sort_by(self):
        """ UT35 - Test codex sort by parameters """
        response = self.client.get('/codex/?sort=base_hp')
        sort_by = response.context['sort_by']
        codex = response.context['codex']
        first_entry = codex[0]
        last_entry = codex[len(codex)-1]
        self.assertTrue(sort_by == 'base_hp')
        self.assertTrue(first_entry.base_hp < last_entry.base_hp)

    def test_codex_edit_view(self):
        """ UT36 - Test codex Edit view """
        # Set user to superuser
        self.user.is_superuser = True
        self.user.save()
        User = get_user_model()
        self.user = User.objects.get(username=self.user.username)
        # Navigate to the 1st Codex entry edit view
        response = self.client.get('/codex/edit/1/')
        # Verify response, template, and object
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/edit.html')
        self.assertTrue(response.context['object'].pk == 1)

    def test_codex_create_view(self):
        """ UT37 - Test codex Create view """
        # Set user to superuser
        self.user.is_superuser = True
        self.user.save()
        User = get_user_model()
        self.user = User.objects.get(username=self.user.username)
        # Navigate to the 1st Codex entry edit view
        response = self.client.get('/codex/create/')
        # Verify response and template
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'codex/create.html')

    def test_codex_delete_view(self):
        """ UT38 - Test codex Delete view """
        # Set user to superuser
        self.user.is_superuser = True
        self.user.save()
        User = get_user_model()
        all_entries = len(Codex.objects.all())
        self.user = User.objects.get(username=self.user.username)
        # Navigate to the 1st Codex entry edit view
        response = self.client.post('/codex/delete/1/')
        # Verify response, template, and object
        self.assertTrue(response.status_code, 200)
        less_entries = len(Codex.objects.all())
        self.assertTrue(all_entries > less_entries)
