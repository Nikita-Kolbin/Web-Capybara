from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'category')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'speciality', 'about', 'link')
    list_display_links = ('user', 'avatar', 'speciality', 'about', 'link')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    list_display_links = ('post', 'image')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
