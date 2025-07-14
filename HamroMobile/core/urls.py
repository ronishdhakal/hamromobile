from django.urls import path
from .views import (
    PhoneFilterView,
    ReviewFilterView,
    NewsFilterView
)

urlpatterns = [
    path('phones/', PhoneFilterView.as_view(), name='phone-filter'),
    path('reviews/', ReviewFilterView.as_view(), name='review-filter'),
    path('news/', NewsFilterView.as_view(), name='news-filter'),
]
