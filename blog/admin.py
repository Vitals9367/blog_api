from django.contrib import admin
from blog.models import Post

# class AuthorAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Post)