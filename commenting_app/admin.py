from django.contrib import admin

from commenting_app.models import UserProfile, Comment


admin.site.register(UserProfile)
admin.site.register(Comment)
