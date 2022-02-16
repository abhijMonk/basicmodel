from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):

    class Types(models.TextChoices):
        UNCLASSIFIED= 'UF', _('UNCLASSIFIED')
        AUDIO = 'AD', _('AUDIO')
        VIDEO = 'VD', _('VIDEO')
        TEXT = 'XT', _('TEXT')

    types_cat = models.CharField(
        max_length=2,
        choices=Types.choices,
        default=Types.UNCLASSIFIED,
    )

    def __str__(self):
        return self.types_cat
