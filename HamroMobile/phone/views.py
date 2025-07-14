from rest_framework import generics
from .models import Phone
from .serializers import PhoneSerializer


class PhoneListAPIView(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneDetailAPIView(generics.RetrieveAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    lookup_field = 'slug'
