from rest_framework import generics
from django.db.models import Min
from django_filters import rest_framework as django_filters

from phone.models import Phone
from review.models import Review
from news.models import News

from phone.serializers import PhoneSerializer
from review.serializers import ReviewSerializer
from news.serializers import NewsSerializer


# ----------------------
# PHONE FILTERS & VIEW
# ----------------------

class PhoneFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name="brand__slug", lookup_expr='iexact')
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr='iexact')
    segment = django_filters.CharFilter(field_name="segment__slug", lookup_expr='iexact')
    type = django_filters.CharFilter(method='filter_by_type')
    price = django_filters.NumberFilter(method='filter_by_price')
    slug = django_filters.CharFilter(field_name="slug", lookup_expr='iexact')

    class Meta:
        model = Phone
        fields = []

    def filter_by_type(self, queryset, name, value):
        return queryset.filter(types__slug=value).distinct()

    def filter_by_price(self, queryset, name, value):
        return queryset.annotate(
            min_price=Min('price_variants__price_npr')
        ).filter(min_price__lte=value)


class PhoneFilterView(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filterset_class = PhoneFilter


# ----------------------
# REVIEW FILTERS & VIEW
# ----------------------

class ReviewFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name="brand__slug", lookup_expr='iexact')
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr='iexact')
    segment = django_filters.CharFilter(field_name="segment__slug", lookup_expr='iexact')
    slug = django_filters.CharFilter(field_name="slug", lookup_expr='iexact')
    ordering = django_filters.OrderingFilter(
        fields=(('sections__rating', 'rating'),)
    )

    class Meta:
        model = Review
        fields = []


class ReviewFilterView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_class = ReviewFilter


# ----------------------
# NEWS FILTERS & VIEW
# ----------------------

class NewsFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(field_name="brand__slug", lookup_expr='iexact')
    category = django_filters.CharFilter(field_name="category__slug", lookup_expr='iexact')
    segment = django_filters.CharFilter(field_name="segment__slug", lookup_expr='iexact')
    slug = django_filters.CharFilter(field_name="slug", lookup_expr='iexact')

    class Meta:
        model = News
        fields = []


class NewsFilterView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterset_class = NewsFilter
