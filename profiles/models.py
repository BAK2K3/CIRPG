from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile Model
    -----------

    Model for all User Profiles:

    user = Link to User model
    paid = Bool to represent paid user
    active_char = Bool to represent whether has an active char
    active_battle = Bool to represent whether user is in a battle
    total_runs = Int to represent total game attempts
    longest_run = Int to represent single high score

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    active_char = models.BooleanField(default=False)
    active_battle = models.BooleanField(default=False)
    total_runs = models.IntegerField(default=0)
    longest_run = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
