from rest_framework import generics
from .models import News
from .serializers import NewsSerializer

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-published_date')
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'
