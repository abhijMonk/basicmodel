from django.db import models

# Create your models here.

class Author(models.Model):
#    author_id = models.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + self.last_name

    def about_the_author(self):
        return self.about