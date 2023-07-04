from django.contrib import admin
from django.contrib.admin import ModelAdmin

from commenting_app.models import Author, Comment


class CommentAdmin(ModelAdmin):
    list_display = ["author", "text", "likes"]


admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)
