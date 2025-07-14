from rest_framework import generics
from .models import Type
from .serializers import TypeSerializer

class TypeListCreateView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    lookup_field = 'slug'
