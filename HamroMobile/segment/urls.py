from django.urls import path
from . import views

urlpatterns = [
    path('', views.SegmentListView.as_view(), name='segment-list'),
    path('<slug:slug>/', views.SegmentDetailView.as_view(), name='segment-detail'),
]
