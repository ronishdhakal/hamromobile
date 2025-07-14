from rest_framework import serializers
from .models import Review, ReviewSection, ReviewSectionGallery

class ReviewSectionGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSectionGallery
        fields = ['id', 'image', 'caption']


class ReviewSectionSerializer(serializers.ModelSerializer):
    gallery = ReviewSectionGallerySerializer(many=True, read_only=True)

    class Meta:
        model = ReviewSection
        fields = ['id', 'name', 'rating', 'text', 'gallery']


class ReviewSerializer(serializers.ModelSerializer):
    sections = ReviewSectionSerializer(many=True, read_only=True)
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    segment_name = serializers.CharField(source='segment.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'title', 'slug', 'featured_image', 'featured',
            'brand', 'brand_name', 'category', 'category_name', 'segment', 'segment_name',
            'summary', 'sections'
        ]
