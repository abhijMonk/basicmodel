from django.db import models
from . author import Author
from . blog import Blog
from . category import Category

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=5000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + "is a" + self.type + "blog"

    def get_the_author(self):
        return self.author

    def get_the_blog(self):
        return self.blog

    def get_the_body(self):
        return self.body

    def get_the_type(self):
        return self.type
