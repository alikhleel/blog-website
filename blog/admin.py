from django.contrib import admin

from .models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')

