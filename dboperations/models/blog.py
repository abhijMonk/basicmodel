from django.db import models
from .author import Author
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Types(models.TextChoices):
        PREGNANCY = 'PR', _('PREGNANCY')
        BABY = 'AB', _('BABY')
        KIDS = 'KD', _('KIDS')
        BEAUTY = 'BT', _('BEAUTY')
        MUMSLIFE = 'ML', _('MUMSLIFE')
        TRAVEL = 'TR', _('TRAVEL')
        RECIPES = 'RC', _('RECIPES')
        HEALTH = 'HL', _('HEALTH')

    types = models.CharField(
        max_length=2,
        choices=Types.choices,
        default=Types.PREGNANCY,
    )

    date_created = models.DateTimeField('Date Created')

    def __str__(self):
        return self.name

    def blog_created_on(self):
        return self.date_created

    def type_of_blog(self):
        return self.types

    def author_of_blog(self):
        return self.author
