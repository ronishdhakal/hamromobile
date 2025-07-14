from django.urls import path
from .views import PhoneListAPIView, PhoneDetailAPIView

urlpatterns = [
    path('', PhoneListAPIView.as_view(), name='phone-list'),
    path('<slug:slug>/', PhoneDetailAPIView.as_view(), name='phone-detail'),
]
