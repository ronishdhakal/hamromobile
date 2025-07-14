from django.contrib import admin
from .models import Type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
