from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'category', 'segment', 'published_date', 'modified_date']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'slug']
    list_filter = ['brand', 'category', 'segment', 'published_date']
