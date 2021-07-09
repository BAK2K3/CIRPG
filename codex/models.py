from django.db import models
from django.utils.translation import gettext_lazy as _


class CodexQuerySet(models.QuerySet):
    """
    Codex Query Set
    -----------

    Codex Query Set for all variants
    of queries and their associated business
    logic
    """

    def custom_filter(self, search_params, sort_params):
        return self.filter(**search_params).order_by(sort_params)


class CodexManager(models.Manager):
    """
    Codex Manager
    -----------

    Codex Manager for calling the custom
    Codex Query Sets
    """

    def get_queryset(self):
        return CodexQuerySet(self.model, using=self._db)

    def filter_queryset(self, search_params, sort_params):
        return (
                self.get_queryset().custom_filter(search_params, sort_params)
        )


class Codex(models.Model):
    """
    Codex Model
    -----------

    Model for all entries within the Codex:

    name = Entry Name
    alpha_name = Organised Name
    type = Choice of Enemy, Weapon, or Hero
    base_hp = Base Hit Points of entry
    base_attack = Base Speed of entry
    base_defense = Base Defense of entry
    base_speed = Base Speed of entry
    image = Image name of entry
    paid = Bool to confirm whether premium entry
    min_level = User's minimum level threshold.
    """

    class Meta:
        verbose_name_plural = 'Codex'

    class TypeChoices(models.TextChoices):
        ENEMY = 'Enemy', _('Enemy')
        WEAPON = 'Weapon', _('Weapon')
        HERO = 'Hero', _('Hero')

    name = models.CharField(max_length=100)
    alpha_name = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TypeChoices.choices,
                            default=TypeChoices.ENEMY)
    base_hp = models.IntegerField(default=5)
    base_attack = models.IntegerField(default=5)
    base_defense = models.IntegerField(default=5)
    base_speed = models.IntegerField(default=5)
    image = models.ImageField()
    paid = models.BooleanField(default=False)
    min_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)],
                                    null=True, blank=True)
    objects = CodexManager()

    def __str__(self):
        return self.name
