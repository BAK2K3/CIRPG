from django.dispatch import receiver
from allauth.account.signals import email_confirmed
from django.contrib.auth import get_user_model

from .models import Profile


@receiver(email_confirmed)
def create_profile(request, email_address, **kwargs):
    """ Create a Profile when a user signs up """
    UserModel = get_user_model()
    user = UserModel.objects.get(emailaddress=email_address)
    Profile.objects.create(user=user)
