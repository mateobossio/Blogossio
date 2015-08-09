from django.contrib import admin

# Register your models here.

from Blog.models import Categoria, Post, Coment

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Coment)