from django.contrib import admin
from rest_blog.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)