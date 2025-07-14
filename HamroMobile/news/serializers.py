from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    segment_name = serializers.CharField(source='segment.name', read_only=True)

    class Meta:
        model = News
        fields = [
            'id', 'title', 'slug', 'brand', 'brand_name',
            'category', 'category_name', 'segment', 'segment_name',
            'content', 'published_date', 'modified_date'
        ]
