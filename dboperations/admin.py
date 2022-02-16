from django.contrib import admin

# Register your models here.

from .models import Author
from .models import Blog
from .models import Category
from .models import Articles

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Articles)
