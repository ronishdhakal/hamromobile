from rest_framework import serializers
from .models import (
    Phone, PriceVariant, GalleryImage, CameraSample,
    PhoneSpecSection, PhoneSpecTitle, PhoneSpecValue
)
from type.models import Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title', 'slug']


class PhoneSpecValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneSpecValue
        fields = ['id', 'value']


class PhoneSpecTitleSerializer(serializers.ModelSerializer):
    values = PhoneSpecValueSerializer(many=True, read_only=True)

    class Meta:
        model = PhoneSpecTitle
        fields = ['id', 'title', 'values']


class PhoneSpecSectionSerializer(serializers.ModelSerializer):
    titles = PhoneSpecTitleSerializer(many=True, read_only=True)

    class Meta:
        model = PhoneSpecSection
        fields = ['id', 'section_name', 'titles']


class PriceVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariant
        fields = ['id', 'ram', 'storage', 'price_npr']


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']


class CameraSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraSample
        fields = ['id', 'image']


class PhoneSerializer(serializers.ModelSerializer):
    price_variants = PriceVariantSerializer(many=True, read_only=True)
    gallery_images = GalleryImageSerializer(many=True, read_only=True)
    camera_samples = CameraSampleSerializer(many=True, read_only=True)
    spec_sections = PhoneSpecSectionSerializer(many=True, read_only=True)
    types = TypeSerializer(many=True, read_only=True)

    class Meta:
        model = Phone
        fields = [
            'id', 'name', 'slug', 'brand', 'category', 'segment',
            'priority', 'meta_title', 'meta_description',
            'display_title', 'display_value',
            'camera_title', 'camera_value',
            'processor_title', 'processor_value',
            'battery_title', 'battery_value',
            'memory_title', 'memory_value',
            'fiveg_title', 'has_5g',
            'types', 'features_image', 'created_at',
            'price_variants', 'gallery_images', 'camera_samples', 'spec_sections', 'buy_link',
        ]
