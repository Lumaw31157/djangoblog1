from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "created_at")
    list_filter = ("status", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
