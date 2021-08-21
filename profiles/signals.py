"""
Profiles App - Signals
----------------

Signals for Profiles App.
    - create_profile
    - admin_profile
"""

from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from .models import Profile


USER_MODEL = get_user_model()


@receiver(email_confirmed)
def create_profile(request, email_address, **kwargs):
    """ Create a Profile when a user signs up """
    user_model = get_user_model()
    user = user_model.objects.get(emailaddress=email_address)
    Profile.objects.create(user=user)


@receiver(post_save, sender=USER_MODEL)
def admin_profile(instance, created, **kwargs):
    """ Create a Profile when a Superuser is created """
    if created and instance.is_superuser:
        Profile.objects.create(user=instance)
