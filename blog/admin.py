from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class SendingAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'count_views')
