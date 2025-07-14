from rest_framework import generics
from .models import Segment
from .serializers import SegmentSerializer

class SegmentListView(generics.ListAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer

class SegmentDetailView(generics.RetrieveAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer
    lookup_field = 'slug'
