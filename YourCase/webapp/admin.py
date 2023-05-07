from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'category')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

