import nested_admin
from django.contrib import admin
from .models import Review, ReviewSection, ReviewSectionGallery

class ReviewSectionGalleryInline(nested_admin.NestedStackedInline):
    model = ReviewSectionGallery
    extra = 1


class ReviewSectionInline(nested_admin.NestedStackedInline):
    model = ReviewSection
    extra = 1
    inlines = [ReviewSectionGalleryInline]


@admin.register(Review)
class ReviewAdmin(nested_admin.NestedModelAdmin):
    list_display = ['title', 'brand', 'category', 'segment', 'featured']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ReviewSectionInline]
