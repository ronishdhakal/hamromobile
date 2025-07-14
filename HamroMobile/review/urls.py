from django.urls import path
from .views import ReviewListView, ReviewDetailView

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('<slug:slug>/', ReviewDetailView.as_view(), name='review-detail'),
]
