from django.contrib import admin
import nested_admin
from .models import (
    Phone,
    PriceVariant,
    GalleryImage,
    CameraSample,
    PhoneSpecSection,
    PhoneSpecTitle,
    PhoneSpecValue
)

class PhoneSpecValueInline(nested_admin.NestedTabularInline):
    model = PhoneSpecValue
    extra = 1
    classes = ['collapse']


class PhoneSpecTitleInline(nested_admin.NestedStackedInline):
    model = PhoneSpecTitle
    extra = 1
    inlines = [PhoneSpecValueInline]
    classes = ['collapse']


class PhoneSpecSectionInline(nested_admin.NestedStackedInline):
    model = PhoneSpecSection
    extra = 1
    inlines = [PhoneSpecTitleInline]
    classes = ['collapse']


class PriceVariantInline(nested_admin.NestedTabularInline):
    model = PriceVariant
    extra = 1
    classes = ['collapse']


class GalleryImageInline(nested_admin.NestedTabularInline):
    model = GalleryImage
    extra = 1
    classes = ['collapse']


class CameraSampleInline(nested_admin.NestedTabularInline):
    model = CameraSample
    extra = 1
    classes = ['collapse']


@admin.register(Phone)
class PhoneAdmin(nested_admin.NestedModelAdmin):
    list_display = ['name', 'brand', 'category', 'segment', 'priority']
    search_fields = ['name', 'slug']
    filter_horizontal = ('types',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'brand', 'category', 'segment', 'priority')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
        ('Key Features', {
            'fields': (
                ('display_title', 'display_value'),
                ('camera_title', 'camera_value'),
                ('processor_title', 'processor_value'),
                ('battery_title', 'battery_value'),
                ('memory_title', 'memory_value'),
                ('fiveg_title', 'has_5g'),
                'buy_link',  # <-- ADDED buy link here
                'types'
            ),
            'classes': ('collapse',),
        }),
        ('Images', {
            'fields': ('features_image',),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at',)

    inlines = [
        PriceVariantInline,
        GalleryImageInline,
        CameraSampleInline,
        PhoneSpecSectionInline
    ]
