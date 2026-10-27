from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published")
    search_fields = ("title", "content")
    list_filter = ("categories", "author")


admin.site.register(Category)
admin.site.register(Post, PostAdmin)